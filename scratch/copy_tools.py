import os
import shutil

src_dirs = [
    r"images\tools",
    r"images\courses\content-video\tools",
    r"images\courses\brand-design\tools",
    r"images\courses\business-marketing\tools"
]

dest_folders = [
    r"images\courses\digital-marketing\tools",
    r"images\courses\graphic-design\tools",
    r"images\courses\video-editing\tools",
    r"images\courses\digital-art\tools",
    r"images\courses\ui-ux\tools",
    r"images\courses\ai-everyone\tools",
    r"images\courses\ar-vr\tools"
]

# Ensure destination folders exist
for dest in dest_folders:
    os.makedirs(dest, exist_ok=True)
    print(f"Created directory: {dest}")

# Copy all files from all source directories to all destination directories
for src in src_dirs:
    if not os.path.exists(src):
        continue
    for file_name in os.listdir(src):
        src_file = os.path.join(src, file_name)
        if os.path.isfile(src_file):
            for dest in dest_folders:
                dest_file = os.path.join(dest, file_name)
                # Copy file if it doesn't already exist or to overwrite with latest
                shutil.copy2(src_file, dest_file)

print("Copy completed successfully!")
