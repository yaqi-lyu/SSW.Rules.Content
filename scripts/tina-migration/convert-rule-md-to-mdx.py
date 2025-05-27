import os
import re
from pathlib import Path

# ----------------------------- #
# Regex patterns for replacement
# ----------------------------- #

YOUTUBE_BLOCK_REGEX = r'`youtube:\s*(https?://[^\s]+)`\s*\n\*\*(.*?)\*\*'
IMAGE_BLOCK_REGEX = r'::: (bad|ok|good)\s+(!\[Figure:.*?\]\(.*?\))\s+:::'
STANDALONE_IMAGE_REGEX = r'!\[Figure:\s*(.*?)\]\((.*?)\)'
EMAIL_BLOCK_REGEX = (
    r'::: email-template\s+(.*?)'
    r'::: email-content\s+(.*?)'
    r':::\s+:::\s+'
    r'(:::\s*(good|bad|ok).*?:::)'
)

BOX_WITH_FIGURE_LINE_REGEX = (
    r':::\s*(greybox|highlight|china|info|todo|codeauditor)\s*\n' 
    r'([^\n]*?(?:\n(?!:::).*)*?)' 
    r'\n:::\s*\n'                        
    r'\*\*Figure:\s*(.*?)\*\*(?=\n|$)'
)
BOX_WITH_CAPTIONS_BLOCK_REGEX = (
    r':::\s*(greybox|highlight|china|info|todo|codeauditor)\s+(.+?)\s+:::\s*'
    r':::\s*(ok|good|bad)\s+Figure:\s*(.+?)\s+:::'
)
BOX_WITHOUT_FIGURE_REGEX = (
    r':::\s*(greybox|highlight|china|info|todo|codeauditor)\s*\n'
    r'([^\n]*?(?:\n(?!:::).*)*?)'
    r'\n:::\s*(?=\n|$)'
)
SIMPLE_FIGURE_BLOCK_REGEX = (
    r':::\s*(good|bad|ok)\s*\n'
    r'([^\n]*?(?:\n(?!:::).*)*?)'
    r'\n:::\s*'
)

# ----------------------------- #
# Utility Functions
# ----------------------------- #

def parse_email_table(table_text):
    """Extract email fields from a markdown-style table."""
    result = {'to': '', 'cc': '', 'bcc': '', 'subject': ''}
    for line in table_text.splitlines():
        parts = line.split('|')
        if len(parts) < 3:
            continue
        key = parts[1].replace(":", "").strip().lower()
        value = parts[2].strip()
        value = mdx_safe_template_vars(value)
        if key in result:
            result[key] = value
    # print(f"Parsed email table header: {result}")
    return result

def clean_email_body(body_text):
    """Prepare the email content block."""
    body_cleaned = mdx_safe_template_vars(body_text)
    return re.sub(r'^###', '##', body_cleaned, flags=re.MULTILINE)

def mdx_safe_template_vars(text):
    # return re.sub(r'{{(.*?)}}', r'`{{\1}}`', text)
    return text.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")

# ----------------------------- #
# Replacement Functions
# ----------------------------- #

def replace_youtube_block(match):
    url = match.group(1).strip()
    description = match.group(2).strip()
    return f'<youtubeEmbed url="{url}" description="{description}" />'

def replace_image_block(match):
    preset = match.group(1).strip()
    image_line = match.group(2).strip()
    alt_match = re.match(r'!\[Figure:\s*(.*?)\]\((.*?)\)', image_line)

    if not alt_match:
        return match.group(0)

    figure = alt_match.group(1).strip()
    raw_src = alt_match.group(2).strip()

    src_match = re.match(r'^([^"\s]+?\.(?:png|jpg|jpeg|gif|webp|svg))', raw_src, re.IGNORECASE)
    src = src_match.group(1) if src_match else raw_src

    return f'''<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{{{
    preset: "{preset}Example",
    figure: "{figure}",
    shouldDisplay: true
  }}}}
  src="{src}"
/>'''

def replace_standalone_image(match):
    figure = match.group(1).strip()
    src = match.group(2).strip()

    return f'''<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{{{
    preset: "default",
    figure: "{figure}",
    shouldDisplay: true
  }}}}
  src="{src}"
/>'''

def replace_email_block(match):
    email_table = match.group(1)
    email_body = match.group(2).strip()
    figure_block = match.group(3)

    email_data = parse_email_table(email_table)
    body_cleaned = clean_email_body(email_body)

    # Parse figure block info
    should_display = 'Figure:' in figure_block
    preset_match = re.match(r'::: (good|bad|ok)', figure_block.strip())
    preset = f"{preset_match.group(1)}Example" if preset_match else "goodExample"

    figure_text_match = re.search(r'Figure:\s*(.*?)\n', figure_block)
    figure_text = figure_text_match.group(1).strip() if figure_text_match else "Email Example"

    return f'''<emailEmbed
  to="{email_data['to']}"
  cc="{email_data['cc']}"
  bcc="{email_data['bcc']}"
  subject="{email_data['subject']}"
  body={{<>
    {body_cleaned}
  </>}}
  figureEmbed={{{{
    preset: "{preset}",
    figure: "{figure_text}",
    shouldDisplay: {"true" if should_display else "false"}
  }}}}
/>'''

def replace_box_with_figure_line(match):
    variant = match.group(1).strip()
    body_text = match.group(2).strip()
    figure = match.group(3).strip()

    print(f"Replacing box with figure line with variant: {variant}, figure: {figure}")

    return f'''<asideEmbed
  variant="{variant}"
  body={{<>
    {body_text}
  </>}}
  figureEmbed={{ {{
    preset: "default",
    figure: "{figure}",
    shouldDisplay: true
  }} }}
/>'''

def replace_box_block(match):
    variant = match.group(1).strip()
    body_text = match.group(2).strip()
    preset = match.group(3).strip() + "Example"
    figure = match.group(4).strip()

    print(f"Replacing box block with variant: {variant}, preset: {preset}, figure: {figure}")

    return f'''<asideEmbed
  variant="{variant}"
  body={{<>
    {body_text}
  </>}}
  figureEmbed={{ {{
    preset: "{preset}",
    figure: "{figure}",
    shouldDisplay: true
  }} }}
/>'''

def replace_box_without_figure(match):
    variant = match.group(1).strip()
    body_text = match.group(2).strip()

    print(f"Replacing box without figure: variant={variant}")

    return f'''<asideEmbed
  variant="{variant}"
  body={{<>
    {body_text}
  </>}}
  figureEmbed={{ {{
    preset: "default",
    figure: "XXX",
    shouldDisplay: false
  }} }}
/>'''

def replace_simple_figure_block(match):
    preset = match.group(1).strip()
    figure = match.group(2).strip()

    return f'''<figureEmbed figureEmbed={{ {{
  preset: "{preset}Example",
  figure: "{figure}",
  shouldDisplay: true
}} }} />\n'''

# ----------------------------- #
# Main Transform Function
# ----------------------------- #

def transform_rule_md_to_mdx(file_path='../../rules/rule/rule.md'):
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {file_path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove <!--endintro--> line
    content = re.sub(r'^\s*<!--endintro-->\s*\n?', '', content, flags=re.MULTILINE)

    # Apply replacements
    content = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, content, flags=re.MULTILINE)
    content = re.sub(IMAGE_BLOCK_REGEX, replace_image_block, content, flags=re.DOTALL)
    content = re.sub(STANDALONE_IMAGE_REGEX, replace_standalone_image, content)
    content = re.sub(EMAIL_BLOCK_REGEX, replace_email_block, content, flags=re.DOTALL)
    content = re.sub(SIMPLE_FIGURE_BLOCK_REGEX, replace_simple_figure_block, content, flags=re.DOTALL)

    content = re.sub(BOX_WITH_FIGURE_LINE_REGEX, replace_box_with_figure_line, content, flags=re.DOTALL)
    content = re.sub(BOX_WITH_CAPTIONS_BLOCK_REGEX, replace_box_block, content, flags=re.DOTALL)
    print("Before BOX_WITH_FIGURE_LINE_REGEX replacement")
    content = re.sub(BOX_WITHOUT_FIGURE_REGEX, replace_box_without_figure, content, flags=re.DOTALL)
    print("After BOX_WITH_FIGURE_LINE_REGEX replacement")

    # Write output as .mdx
    output_path = path.with_suffix('.mdx')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Transformed content saved to: {output_path}")

# ----------------------------- #
# Entry point
# ----------------------------- #

if __name__ == '__main__':
    transform_rule_md_to_mdx()
