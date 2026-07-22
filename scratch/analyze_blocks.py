import os
import re

files = [
    "graphic-design-course.html",
    "video-editing-course.html",
    "digital-marketing-course.html",
    "courses/digital-marketing-course-siliguri.html"
]

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"

for file_path in files:
    full_path = os.path.join(base_dir, file_path)
    if not os.path.exists(full_path):
        continue
    
    print(f"\n==================== {file_path} ====================")
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Locate HTML start & end
    html_match = re.search(r'<section class="testi-section[^>]*>', content)
    if html_match:
        start_idx = html_match.start()
        # Find closing </section>
        # Let's count sections or find the closing tag
        end_idx = content.find('</section>', start_idx) + len('</section>')
        print(f"HTML block starts at index {start_idx} (line {content.count('\n', 0, start_idx) + 1})")
        print(f"HTML block ends at index {end_idx} (line {content.count('\n', 0, end_idx) + 1})")
        # Print first and last line of html block
        lines = content[start_idx:end_idx].split('\n')
        print(f"First HTML line: {lines[0]}")
        print(f"Last HTML line: {lines[-1]}")
    else:
        print("HTML block not found")
        
    # Locate JS block
    js_match = re.search(r'// ─── TESTIMONIALS COVERFLOW INTERACTION SYSTEM ───', content)
    if js_match:
        start_idx = js_match.start()
        end_idx = content.find('</script>', start_idx)
        print(f"JS block starts at index {start_idx} (line {content.count('\n', 0, start_idx) + 1})")
        print(f"JS block ends at index {end_idx} (line {content.count('\n', 0, end_idx) + 1})")
    else:
        print("JS block not found")
        
    # Locate CSS block
    css_match = re.search(r'/\* Testimonials Section \*/|/\* ─── TESTIMONIALS 3D COVERFLOW REDESIGN ─── \*/', content)
    if css_match:
        start_idx = css_match.start()
        print(f"CSS block starts at index {start_idx} (line {content.count('\n', 0, start_idx) + 1})")
    else:
        print("CSS block not found")
