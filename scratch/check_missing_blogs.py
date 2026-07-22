import os
import re

blogs_dir = "/Users/isharoka/Downloads/MAin website/blogs"
blog_html_path = "/Users/isharoka/Downloads/MAin website/blog.html"

with open(blog_html_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

all_folders = []
for name in os.listdir(blogs_dir):
    if name.startswith("."):
        continue
    path = os.path.join(blogs_dir, name)
    if os.path.isdir(path):
        # check if index.html exists inside
        if os.path.exists(os.path.join(path, "index.html")):
            all_folders.append(name)

print("Total blog folders with index.html:", len(all_folders))

missing = []
for folder in all_folders:
    # check if the folder slug exists in blog_content
    # e.g., blog/folder/ or blog/some-subpath/folder/ or blogs/folder/
    pattern = re.compile(rf"{re.escape(folder)}/?['\"]")
    # or just simple substring check
    if folder not in blog_content:
        missing.append(folder)

print("\nMissing blogs from blog.html:")
for folder in sorted(missing):
    print("-", folder)
