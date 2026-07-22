import os
import re

html_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"

# List of HTML files to process
html_files = [f for f in os.listdir(html_dir) if f.endswith(".html")]

replacements = {
    "/course/graphic-design-course": "/course/graphic-design-course-siliguri",
    "/course/video-editing-course": "/course/video-motion-course-siliguri",
    "/course/digital-marketing-course": "/course/digital-marketing-course-siliguri",
    "/course/ai-for-everyone": "/course/ai-for-everyone-siliguri",
    "/course/ar-vr-course": "/course/ar-vr-course-siliguri",
    "/course/the-digital-art-course": "/course/the-digital-art-course-siliguri",
    "/course/the-ui-ux-design-course": "/course/the-ui-ux-design-course-siliguri"
}

for file_name in html_files:
    file_path = os.path.join(html_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    for old_path, new_path in replacements.items():
        # Avoid replacing if it already has -siliguri
        # We can use regex to match old_path followed by optional -siliguri and replace it with new_path
        pattern = re.escape(old_path) + r"(?!-siliguri)\b"
        new_content, count = re.subn(pattern, new_path, content)
        if count > 0:
            content = new_content
            modified = True
            print(f"Replaced {count} occurrences of {old_path} in {file_name}")
            
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Done scanning and replacing in HTML files.")
