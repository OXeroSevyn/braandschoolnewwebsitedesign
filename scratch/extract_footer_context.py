import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's write the surrounding 2000 characters before and after the <footer tag to a scratch file
footer_pos = content.find("<footer")
if footer_pos != -1:
    start = max(0, footer_pos - 1500)
    end = min(len(content), footer_pos + 1500)
    context = content[start:end]
    with open("scratch/footer_context.txt", "w", encoding="utf-8") as out:
        out.write(context)
    print("Footer context written to scratch/footer_context.txt")
else:
    print("Footer not found")
