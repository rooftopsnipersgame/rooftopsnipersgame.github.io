import os
import re

def modify_iframe_sources(directory_path):
    # Regular expression to match iframe tags with specific src pattern
    iframe_pattern = re.compile(
        r'(<iframe [^>]*src=")\.\./([^"]+)/index\.html(" [^>]*>)', re.IGNORECASE)

    # Function to replace the matched groups
    def replacement(match):
        # Construct new src attribute value, ensuring the trailing slash is kept
        new_src = 'https://just-fall.github.io/' + match.group(2) + '/'
        # Return the updated iframe tag
        return match.group(1) + new_src + match.group(3)

    # List all html files and apply the replacement
    for filename in os.listdir(directory_path):
        if filename.endswith('.html'):  # Check for HTML files
            file_path = os.path.join(directory_path, filename)

            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Replace the src attributes within iframe tags
            updated_content = iframe_pattern.sub(replacement, content)

            # Write the changes back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

    print("All iframe sources have been updated.")

# Specify the path to your directory
directory_path = '/Applications/XAMPP/xamppfiles/htdocs/GitHubChrome/rooftopsnipersgame.github.io/go'

# Attempt to modify the iframe sources
try:
    modify_iframe_sources(directory_path)
except FileNotFoundError:
    print("The specified directory was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
