import os

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
file_path = os.path.join(base_dir, "graphic-design-course.html")

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1219, min(1270, len(lines))):
    print(f"{i+1}: {lines[i].strip()}")
