import os

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
index_html = os.path.join(base_dir, "index.html")

with open(index_html, 'r', encoding='utf-8') as f:
    content = f.read()

if "fg-bg-container" in content:
    print("Found fg-bg-container in HTML/CSS")
    # Let's count occurences in HTML vs CSS
    print("HTML occurrences:", content.count('<div class="fg-bg-container"'))
    print("CSS occurrences:", content.count('.fg-bg-container'))
else:
    print("Not found")
