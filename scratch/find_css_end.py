import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
file_path = os.path.join(base_dir, "graphic-design-course.html")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find("/* Testimonials Section */")
if start_idx != -1:
    chunk = content[start_idx:start_idx+10000]
    next_comment = chunk.find("/*", 50)
    if next_comment != -1:
        print("Next comment starts at index:", start_idx + next_comment)
        print(content[start_idx : start_idx + next_comment + 50])
    else:
        print("No next comment found in chunk")
else:
    print("Not found")
