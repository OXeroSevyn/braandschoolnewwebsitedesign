import os
import glob

old_filename = "life-at-bs.html"
new_filename = "gallery.html"

# 1. Rename life-at-bs.html to gallery.html
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"Renamed {old_filename} to {new_filename}")
else:
    print(f"Warning: {old_filename} does not exist in root.")

# 2. Update references in all HTML files
html_files = glob.glob("**/*.html", recursive=True)

for filepath in html_files:
    # Skip inside hidden/special directories
    if any(part.startswith('.') or part == 'node_modules' for part in filepath.split(os.sep)):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # Replace filenames
    content = content.replace("life-at-bs.html", "gallery.html")
    
    # Replace link labels for menus
    content = content.replace(">Life at BS<", ">Gallery<")
    content = content.replace(">Life At BS<", ">Gallery<")
    content = content.replace("Life at BS", "Gallery")
    content = content.replace("Life At BS", "Gallery")

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated references in: {filepath}")
