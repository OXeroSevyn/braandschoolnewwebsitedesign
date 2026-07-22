with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Locate life at bs section
life_start = -1
for idx, line in enumerate(lines):
    if "LIFE AT BS PREVIEW SECTION" in line:
        life_start = idx
        break

if life_start == -1:
    print("Could not find start of Life preview section!")
    exit(1)

# Locate end of life at bs section
# It ends with window.addEventListener('scroll', revealWork ... </script> right before FAQ
life_end = -1
for idx in range(life_start + 1, len(lines)):
    if "class=\"faq-section\"" in lines[idx] or "id=\"faq\"" in lines[idx]:
        # Walk back to find the closing </script>
        for j in range(idx - 1, life_start, -1):
            if "</script>" in lines[j]:
                life_end = j
                break
        break

if life_end == -1:
    print("Could not find end of Life preview section!")
    exit(1)

print(f"Extracting Life preview lines {life_start+1} to {life_end+1}...")
life_lines = lines[life_start:life_end+1]

# Delete from document
remaining_lines = lines[:life_start] + lines[life_end+1:]

# Locate the insert index: right after doubt-section styles (which ends on </style> around line 5049)
insert_idx = -1
for idx, line in enumerate(remaining_lines):
    if idx >= 4800 and idx < 5100 and "</style>" in line:
        # Check if the next block is AUTHORIZED SECTION
        if idx + 2 < len(remaining_lines) and "AUTHORIZED SECTION" in remaining_lines[idx + 2]:
            insert_idx = idx
            break

if insert_idx == -1:
    # Fallback: search exactly for "</style>" around 5049 in remaining lines
    for idx, line in enumerate(remaining_lines):
        if idx >= 5035 and idx <= 5055 and "</style>" in line:
            insert_idx = idx
            break

if insert_idx == -1:
    print("Could not find inserting position after doubt-section styles!")
    exit(1)

print(f"Inserting after line {insert_idx+1} in remaining lines...")

# Insert at insert_idx + 1
final_lines = remaining_lines[:insert_idx+1] + ["\n"] + life_lines + remaining_lines[insert_idx+1:]

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(final_lines)

print("Successfully moved Life preview section right after doubts section!")
