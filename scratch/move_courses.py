import os
import re

# Directories
root_dir = r"c:\Subham\aiappsnew\Braand School (Website)"
course_dir = os.path.join(root_dir, "course")

# Create course directory if it doesn't exist
os.makedirs(course_dir, exist_ok=True)

# Files to move
files_to_move = [
    "braanding-course.html",
    "creator-course.html",
    "business-marketing-course.html"
]

root_html_files = [
    "index.html",
    "life-at-bs.html",
    "manifesto.html",
    "studio.html",
    "course.html",
    "content.html"
]

# 1. Update paths in the files that are moving
for filename in files_to_move:
    src_path = os.path.join(root_dir, filename)
    dest_path = os.path.join(course_dir, filename)
    
    if os.path.exists(src_path):
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace assets/, images/, uploads/ paths with ../
        content = re.sub(r'(href|src)="assets/', r'\1="../assets/', content)
        content = re.sub(r'(href|src)="images/', r'\1="../images/', content)
        content = re.sub(r'(href|src)="uploads/', r'\1="../uploads/', content)
        
        # Replace root-level HTML links with ../ except for the moving files
        for root_file in root_html_files:
            content = re.sub(r'href="' + re.escape(root_file) + r'"', r'href="../' + root_file + r'"', content)
            
        # Write to the new destination
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Remove old file
        os.remove(src_path)
        print(f"Moved and updated: {filename} -> course/{filename}")

# 2. Update links pointing to the course files in all other HTML files (in root and in course)
all_html_files_paths = [os.path.join(root_dir, f) for f in root_html_files] + [os.path.join(course_dir, f) for f in files_to_move]

for file_path in all_html_files_paths:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Update references to the moved course files
        # If the file is inside the course/ folder, links to other course files should NOT have 'course/' prepended.
        is_in_course_dir = os.path.dirname(file_path) == course_dir
        
        for course_file in files_to_move:
            if is_in_course_dir:
                # Inside course dir: link should just be 'course_file' (e.g. braanding-course.html)
                # But make sure we don't have '../course/' or similar
                content = re.sub(r'href="\.\./course/' + re.escape(course_file) + r'"', r'href="' + course_file + r'"', content)
                content = re.sub(r'href="course/' + re.escape(course_file) + r'"', r'href="' + course_file + r'"', content)
            else:
                # Outside course dir: link should be 'course/course_file'
                # Avoid double prepending if it's already course/
                content = re.sub(r'href="(?!(course/|\.\./))' + re.escape(course_file) + r'"', r'href="course/' + course_file + r'"', content)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated course links in: {os.path.basename(file_path)}")

print("Done!")
