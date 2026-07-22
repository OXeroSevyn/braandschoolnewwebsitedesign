import os
import re

html_path = "graphic-design-course.html"
tools_dir = "images/tools"

valid_extensions = {".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"}
logos = [f for f in os.listdir(tools_dir) if os.path.splitext(f)[1].lower() in valid_extensions]

logo_html = "".join([f'<div class="tool-logo-box"><img src="images/tools/{logo}" alt="{os.path.splitext(logo)[0]}"></div>' for logo in logos])

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

def replace_marquee_items(match):
    return f'<div class="marquee-items">\n            {logo_html}\n          </div>'

content = re.sub(r'<div class="marquee-items">.*?</div>', replace_marquee_items, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated the marquee with {len(logos)} tools!")
