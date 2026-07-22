import os

replacements = {
    "graphic-design-course.html": [
        ("images/courses/brand-design/tools/", "images/courses/graphic-design/tools/")
    ],
    "video-editing-course.html": [
        ("images/courses/content-video/tools/", "images/courses/video-editing/tools/")
    ],
    "digital-marketing-course.html": [
        ("images/courses/business-marketing/tools/", "images/courses/digital-marketing/tools/")
    ],
    "courses/digital-marketing-course-siliguri.html": [
        ("images/tools/", "images/courses/digital-marketing/tools/")
    ],
    "the-digital-art-course.html": [
        ("/images/tools/", "images/courses/digital-art/tools/")
    ]
}

for file_path, pairs in replacements.items():
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = content
        for old, new in pairs:
            modified = modified.replace(old, new)
        
        if modified != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified)
            print(f"Updated paths in: {file_path}")
        else:
            print(f"No paths needed updating in: {file_path}")
    else:
        print(f"File not found: {file_path}")
