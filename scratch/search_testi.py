import os
import sys

# Set console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

files = [
    "graphic-design-course.html",
    "video-editing-course.html",
    "digital-marketing-course.html",
    "courses/digital-marketing-course-siliguri.html"
]

for file_path in files:
    full_path = os.path.join(r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0", file_path)
    if not os.path.exists(full_path):
        print(f"File not found: {file_path}")
        continue
    
    print(f"\n=== {file_path} ===")
    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line_lower = line.lower()
            if any(term in line_lower for term in ["testimonial", "testi-", "student_"]):
                print(f"Line {idx+1}: {line.strip()[:100]}")
