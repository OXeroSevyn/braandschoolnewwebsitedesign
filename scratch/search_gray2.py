import os

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
main_css = os.path.join(base_dir, "assets", "css", "main.css")

with open(main_css, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if "--gray2" in line:
            print(f"Line {idx+1}: {line.strip()}")
