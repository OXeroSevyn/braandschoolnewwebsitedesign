import os

replacements = [
    ("/course/video-editing-course", "/course/video-motion-course"),
]

# Find all relevant files in the workspace (excluding .git, .vercel, node_modules)
target_files = []
for root, dirs, files in os.walk('.'):
    if any(ignore in root for ignore in ['.git', '.vercel', 'node_modules']):
        continue
    for f in files:
        if f.endswith('.html'):
            target_files.append(os.path.join(root, f))

# Update content
for file_path in target_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        continue
        
    new_content = content
    for target, repl in replacements:
        new_content = new_content.replace(target, repl)
        
    if new_content != content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
