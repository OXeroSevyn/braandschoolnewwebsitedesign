import os

replacements = [
    ("video-editing-course-siliguri", "video-motion-course-siliguri"),
]

# Find all relevant files in the workspace (excluding .git, .vercel, node_modules)
target_files = []
for root, dirs, files in os.walk('.'):
    if any(ignore in root for ignore in ['.git', '.vercel', 'node_modules']):
        continue
    for f in files:
        if f.endswith(('.html', '.json', '.py')):
            target_files.append(os.path.join(root, f))

# Update content in all target files except current script and dev_server.py (handled specifically or generic)
for file_path in target_files:
    if os.path.basename(file_path) == "rename_video_motion.py":
        continue
        
    print(f"Reading: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"  Error reading {file_path}: {e}")
        continue
        
    new_content = content
    for target, repl in replacements:
        new_content = new_content.replace(target, repl)
        
    if new_content != content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Updated: {file_path}")
        except Exception as e:
            print(f"  Error writing {file_path}: {e}")
    else:
        print(f"  No changes: {file_path}")

print("Basic replacements done.")
