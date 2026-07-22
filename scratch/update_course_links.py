import os
import re

root_dir = r"c:\Subham\aiappsnew\Braand School (Website)"

files_to_update = [
    "index.html",
    "life-at-bs.html",
    "manifesto.html",
    "studio.html",
    "course.html",
    "content.html",
    "braanding-course.html",
    "creator-course.html",
    "business-marketing-course.html"
]

mapping = {
    "braanding-course.html": "/course/braanding-course",
    "creator-course.html": "/course/creator-course",
    "business-marketing-course.html": "/course/business-marketing-course"
}

for filename in files_to_update:
    file_path = os.path.join(root_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        for original, new_url in mapping.items():
            # Match href="braanding-course.html" or href='braanding-course.html'
            # We can replace it with href="/course/braanding-course"
            pattern = r'href=["\']' + re.escape(original) + r'["\']'
            replacement = f'href="{new_url}"'
            
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                modified = True
                
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated course links in: {filename}")
        else:
            print(f"No course links found/updated in: {filename}")

print("Done!")
