with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in range(8253, 8270):
    print(f"{idx+1}: {lines[idx].strip().encode('ascii', 'ignore').decode()}")
