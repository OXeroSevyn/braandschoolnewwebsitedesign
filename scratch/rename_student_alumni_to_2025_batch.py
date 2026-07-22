import os
import glob

old_filename = "student-alumni.html"
new_filename = "2025-batch.html"

# 1. Rename student-alumni.html to 2025-batch.html
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"Renamed {old_filename} to {new_filename}")
elif os.path.exists(new_filename):
    print(f"{new_filename} already exists.")
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
    content = content.replace("student-alumni.html", "2025-batch.html")
    
    # Replace link labels for menus
    content = content.replace("Student Alumni", "2025 Batch")
    content = content.replace("student-alumni", "2025-batch")

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated references in: {filepath}")
