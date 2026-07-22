with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(7648, min(7665, len(lines))):
    safe_text = lines[i].encode('ascii', 'ignore').decode()
    print(f"Line {i+1}: {repr(safe_text)}")
