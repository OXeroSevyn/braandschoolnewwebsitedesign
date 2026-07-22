import os
import glob

replacements = {
    "The Graphic Design Course": "Graphic Design Course",
    "The Video Editing Course": "Video Editing Course",
    "The Digital Marketing Course": "Digital Marketing Course",
    "the Graphic Design Course": "Graphic Design Course",
    "the Video Editing Course": "Video Editing Course",
    "the Digital Marketing Course": "Digital Marketing Course",
}

html_files = glob.glob("**/*.html", recursive=True)

for filepath in html_files:
    # Skip inside hidden/special directories
    if any(part.startswith('.') or part == 'node_modules' for part in filepath.split(os.sep)):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {filepath}")
