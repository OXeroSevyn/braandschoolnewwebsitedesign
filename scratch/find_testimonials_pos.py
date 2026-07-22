with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in range(8450, 8560):
    safe_text = lines[idx].encode('ascii', 'ignore').decode()
    print(f"{idx+1}: {repr(safe_text)}")
