import os
import re

files_to_fix = [
    r"video-editing-course.html",
    r"graphic-design-course.html",
    r"digital-marketing-course.html",
    r"courses/digital-marketing-course-siliguri.html"
]

target_pattern = re.compile(
    r'\.modules-wrapper-bg-container::before\s*\{[^}]*background-image:[^}]*\}',
    re.DOTALL
)

replacement = """.modules-wrapper-bg-container::before {
        content: '';
        position: absolute;
        inset: 0;
        /* Removed CPU-heavy SVG turbulence noise for smooth scroll performance */
        opacity: 0;
      }"""

for f_path in files_to_fix:
    if os.path.exists(f_path):
        print(f"Optimizing: {f_path}")
        with open(f_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content = target_pattern.sub(replacement, content)
        if new_content != content:
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("  Successfully updated.")
        else:
            # Fallback if pattern didn't match exactly due to formatting
            print("  Pattern not matched exactly. Trying literal replacement...")
            literal_target = '.modules-wrapper-bg-container::before {'
            # Let's find index of literal_target
            idx = content.find(literal_target)
            if idx != -1:
                end_idx = content.find('}', idx)
                if end_idx != -1:
                    new_content = content[:idx] + replacement + content[end_idx+1:]
                    with open(f_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print("  Successfully updated (literal fallback).")
                else:
                    print("  Could not find matching closing brace.")
            else:
                print("  Could not find modules-wrapper-bg-container::before selector.")
    else:
        print(f"File not found: {f_path}")
