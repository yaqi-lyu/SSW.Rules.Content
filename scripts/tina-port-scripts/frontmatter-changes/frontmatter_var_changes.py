# mostly 🤖🤖🤖🤖 with some modifications
# run python scripts from their directory with python3 <name>.py

import os
import fnmatch

# Function to process markdown files
def match_and_process_frontmatter(func, directory, target_keyword):
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, '*.md'):
            file_path = os.path.join(root, filename)
            print(f"Processing {file_path}")

            # Read the content of the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Prepare to write modified content
            new_lines = []
            in_frontmatter = False
            frontmatter_limit = 2
            for line in lines:
                if line.startswith('---') and frontmatter_limit > 0:
                    in_frontmatter = not in_frontmatter
                    frontmatter_limit -= 1
                # Check for the 'target_keyword: XYZ' pattern
                if line.startswith(target_keyword) and in_frontmatter:
                    # Add on the function result
                    new_lines.append(func(line));
                else:
                    new_lines.append(line)  # Add the original line

            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.writelines(new_lines)
                file.close()
