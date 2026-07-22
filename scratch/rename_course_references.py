import os
import re

replacements = [
    # 1. URL Path and file name replacements
    (r'/course/braanding-course', r'/course/graphic-design-course'),
    (r'/course/creator-course', r'/course/video-editing-course'),
    (r'/course/business-marketing-course', r'/course/digital-marketing-course'),
    
    (r'braanding-course\.html', r'graphic-design-course.html'),
    (r'creator-course\.html', r'video-editing-course.html'),
    (r'business-marketing-course\.html', r'digital-marketing-course.html'),

    # 2. Text Label Replacements (case-sensitive where needed)
    # Brand & Design -> The Graphic Design Course
    (r'>Brand & Design</a>', r'>The Graphic Design Course</a>'),
    (r'>Brand &amp; Design</a>', r'>The Graphic Design Course</a>'),
    (r'"name"\s*:\s*"Brand & Design"', r'"name": "The Graphic Design Course"'),
    (r'"name"\s*:\s*"Brand &amp; Design"', r'"name": "The Graphic Design Course"'),
    
    # Content & Video -> The Video Editing Course
    (r'>Content & Video</a>', r'>The Video Editing Course</a>'),
    (r'>Content &amp; Video</a>', r'>The Video Editing Course</a>'),
    (r'"name"\s*:\s*"Content & Video"', r'"name": "The Video Editing Course"'),
    (r'"name"\s*:\s*"Content &amp; Video"', r'"name": "The Video Editing Course"'),
    
    # Business & Marketing -> The Digital Marketing Course
    (r'>Business & Marketing</a>', r'>The Digital Marketing Course</a>'),
    (r'>Business &amp; Marketing</a>', r'>The Digital Marketing Course</a>'),
    (r'"name"\s*:\s*"Business & Marketing"', r'"name": "The Digital Marketing Course"'),
    (r'"name"\s*:\s*"Business &amp; Marketing"', r'"name": "The Digital Marketing Course"'),
]

# We should search HTML files in current folder and 'courses' subfolder
html_files = []
for root, dirs, files in os.walk('.'):
    # Skip git and vercel dirs
    if '.git' in root or '.vercel' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for file_path in html_files:
    print(f"Processing: {file_path}")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content
    for pattern, repl in replacements:
        new_content = re.sub(pattern, repl, new_content)
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Updated: {file_path}")
    else:
        print(f"  No changes: {file_path}")
