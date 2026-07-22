import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0"
file_path = os.path.join(base_dir, "graphic-design-course.html")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find("/* ─── TESTIMONIALS 3D COVERFLOW REDESIGN ─── */")
if start_idx != -1:
    chunk = content[start_idx:start_idx+10000]
    # Find next comment that doesn't start with coverflow
    # or find closing </style>
    style_close = chunk.find("</style>")
    print("Found coverflow CSS block:")
    print(chunk[:style_close])
else:
    print("Coverflow CSS block not found")
