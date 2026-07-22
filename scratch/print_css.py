import os

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
file_path = os.path.join(base_dir, "graphic-design-course.html")

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
for idx, line in enumerate(lines):
    if "/* Testimonials Section */" in line:
        start_idx = idx
        break

if start_idx != -1:
    print("Found starting line:", start_idx + 1)
    # Print 50 lines from here
    for i in range(start_idx, start_idx + 60):
        print(f"{i+1}: {lines[i].strip()}")
else:
    print("Not found")
