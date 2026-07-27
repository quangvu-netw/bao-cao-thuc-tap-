import os
import re

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return

    # Find all {{ ... }} blocks and remove newlines inside them
    def replace_newlines(match):
        # match.group(0) is the whole {{ ... }} block
        # we replace newline with space, and then remove extra spaces
        text = match.group(0).replace('\n', ' ').replace('\r', ' ')
        return re.sub(r'\s+', ' ', text)

    # Regex to match {{ followed by anything (including newlines) followed by }}
    # using non-greedy *?
    new_content = re.sub(r'\{\{.*?\}\}', replace_newlines, content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

def main():
    # Only fix the layouts directory inside the theme
    directory = os.path.join('themes', 'hugo-theme-learn', 'layouts')
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                fix_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
