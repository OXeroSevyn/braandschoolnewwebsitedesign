with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.finditer(r'[^{}]*quote[^{}]*\{[^{}]*\}', content, re.IGNORECASE)
for m in matches:
    print(m.group(0))
    print("---")
