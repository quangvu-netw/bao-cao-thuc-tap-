import os

replacements = {
    'tranvantrung27@gmail.com': 'thuanh9999.com@gmail.com',
    'trantrung04.contact@gmail.com': 'thuanh9999.com@gmail.com',
    'tranvantrung27': 'quangvu-netw',
    'tranvantrung': 'lamquangvu',
    'trantrung04': 'lamquangvu',
    '-trung-': '-vu-'
}

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    # Bỏ qua các thư mục không cần thiết
    if '.git' in root or 'public' in root or 'themes' in root:
        continue
    for file in files:
        if file.endswith(('.md', '.toml', '.html', '.yaml', '.txt')):
            replace_in_file(os.path.join(root, file))
