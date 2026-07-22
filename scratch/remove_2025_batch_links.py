import os
import re

# Directory containing the site
base_dir = "/Users/isharoka/Downloads/MAin website"

# Regex patterns to remove 2025 Batch menu items
# Pattern 1: Desktop list item
desktop_pattern = re.compile(r'<li>\s*<a\s+[^>]*href=["\']/2025-batch\.html["\'][^>]*>2025 Batch</a>\s*</li>', re.IGNORECASE)

# Pattern 2: Mobile nav items (two possible attribute orders)
mobile_pattern1 = re.compile(r'<a\s+[^>]*href=["\']/2025-batch\.html["\']\s+class=["\']mobile-nav-item["\'][^>]*>2025 Batch</a>', re.IGNORECASE)
mobile_pattern2 = re.compile(r'<a\s+class=["\']mobile-nav-item["\']\s+href=["\']/2025-batch\.html["\'][^>]*>2025 Batch</a>', re.IGNORECASE)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    # Perform replacements
    content = desktop_pattern.sub('', content)
    content = mobile_pattern1.sub('', content)
    content = mobile_pattern2.sub('', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

# Walk through directory
for root, dirs, files in os.walk(base_dir):
    # Skip standard system dirs
    if '.git' in root or '__MACOSX' in root or '.agents' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
