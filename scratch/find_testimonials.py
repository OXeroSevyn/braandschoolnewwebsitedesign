import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'<!-- ── (.*?) ── -->|<section[^>]*>|<div[^>]+class="[^"]*(?:testimonial|review|story|says)[^"]*"', re.IGNORECASE)
for m in pattern.finditer(content):
    line_no = content.count('\n', 0, m.start()) + 1
    safe_text = m.group().encode('ascii', 'ignore').decode()
    print(f"Line {line_no}: {safe_text}")
