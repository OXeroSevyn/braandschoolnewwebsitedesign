import os
import re

root_dir = r"c:\Subham\aiappsnew\Braand School (Website)"

course_files = [
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

# We want to replace href="index.html" with href="/index.html" (or /) inside the course pages
for filename in course_files:
    file_path = os.path.join(root_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        
        # 1. Convert root page links to absolute paths (starting with /)
        for root_file in root_html_files:
            # Match href="index.html" or href='index.html'
            pattern = r'href=["\']' + re.escape(root_file) + r'["\']'
            # For index.html, we can use "/" or "/index.html". Let's use "/index.html" for clarity or "/" for cleaner URLs.
            # Let's use "/index.html" to be safe and consistent with the others.
            replacement = f'href="/{root_file}"'
            
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                modified = True
        
        # 2. Let's make sure the course links themselves are also absolute inside the course pages
        # (e.g. href="braanding-course.html" -> href="/course/braanding-course")
        mapping = {
            "braanding-course.html": "/course/braanding-course",
            "creator-course.html": "/course/creator-course",
            "business-marketing-course.html": "/course/business-marketing-course"
        }
        for orig, new_url in mapping.items():
            pattern = r'href=["\']' + re.escape(orig) + r'["\']'
            replacement = f'href="{new_url}"'
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                modified = True

        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed links to be absolute in: {filename}")
        else:
            print(f"No links updated in: {filename}")

print("Done!")
