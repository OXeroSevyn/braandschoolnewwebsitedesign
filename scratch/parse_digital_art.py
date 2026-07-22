import re

file_path = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\the-digital-art-course.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

idx = html.find("Module 3:")
if idx != -1:
    sub = html[idx-100:idx+4000]
    clean_sub = re.sub(r'<[^>]+>', '\n', sub)
    clean_sub = "\n".join([line.strip() for line in clean_sub.splitlines() if line.strip()])
    print("--- DETAILED MODULES TEXT (PART 2) ---")
    print(clean_sub[:3000])
