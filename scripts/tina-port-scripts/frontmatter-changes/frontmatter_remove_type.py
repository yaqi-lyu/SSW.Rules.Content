# mostly 🤖🤖🤖🤖 with some modifications
# run python scripts from their directory with python3 <name>.py

from frontmatter_var_changes import match_and_process_frontmatter


# Keyword for special handling
KEYWORD = 'type'
# Directory containing markdown files
DIRECTORY = "../../../categories"

def line_func(line):
    return "";

match_and_process_frontmatter(line_func, DIRECTORY, KEYWORD)
