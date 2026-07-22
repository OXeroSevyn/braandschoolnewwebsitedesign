import os

files_to_update = [
    "index.html",
    "course.html",
    "life-at-bs.html",
    "contact.html",
    "braanding-course.html",
    "business-marketing-course.html",
    "creator-course.html",
    "courses/index.html",
    "courses/digital-marketing-course-siliguri.html",
    "scratch/generate_alumni_page.py"
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        print(f"Skipping non-existent file: {filepath}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Desktop link replacements
    desktop_find = '<li><a href="/student-alumni.html">Student Alumni</a></li>'
    desktop_replace = '<li><a href="/student-alumni.html">Student Alumni</a></li>\n        <li><a href="/blogs.html">Blogs</a></li>'
    
    # 2. Mobile link style A replacements
    mobile_find_a = '<a href="/student-alumni.html" class="mobile-nav-item">Student Alumni</a>'
    mobile_replace_a = '<a href="/student-alumni.html" class="mobile-nav-item">Student Alumni</a>\n        <a href="/blogs.html" class="mobile-nav-item">Blogs</a>'
    
    # 3. Mobile link style B replacements
    mobile_find_b = '<a class="mobile-nav-item" href="/student-alumni.html">Student Alumni</a>'
    mobile_replace_b = '<a class="mobile-nav-item" href="/student-alumni.html">Student Alumni</a>\n        <a class="mobile-nav-item" href="/blogs.html">Blogs</a>'

    original_content = content
    content = content.replace(desktop_find, desktop_replace)
    content = content.replace(mobile_find_a, mobile_replace_a)
    content = content.replace(mobile_find_b, mobile_replace_b)

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully updated menu bar in: {filepath}")
    else:
        print(f"No changes made to: {filepath} (links might already exist or format differed)")
