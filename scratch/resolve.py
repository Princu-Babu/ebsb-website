import os
import re

def resolve_conflicts_keep_head():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to match conflict blocks
        # <<<<<<< HEAD\n(content to keep)\n=======\n(content to drop)\n>>>>>>> (commit_hash)\n
        pattern = re.compile(r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>> [a-f0-9]+\n', re.DOTALL)
        
        new_content, count = pattern.subn(r'\1\n', content)
        
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Resolved {count} conflicts in {file}")

if __name__ == "__main__":
    resolve_conflicts_keep_head()
