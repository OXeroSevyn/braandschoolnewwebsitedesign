import os
import glob

# 1. Delete blogs.html
if os.path.exists("blogs.html"):
    os.remove("blogs.html")
    print("Deleted blogs.html file.")
else:
    print("blogs.html was already deleted or doesn't exist.")

# 2. Find all HTML files recursively in the workspace
html_files = glob.glob("**/*.html", recursive=True)

for filepath in html_files:
    # Skip files inside node_modules or .vercel or similar hidden folders
    if any(part.startswith('.') or part == 'node_modules' for part in filepath.split(os.sep)):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # Patterns to remove:
    # Desktop link
    content = content.replace('<li><a href="/blogs.html">Blogs</a></li>', '')
    content = content.replace('<li><a href="blogs.html">Blogs</a></li>', '')
    content = content.replace('<li><a href="./blogs.html">Blogs</a></li>', '')

    # Mobile link style A
    content = content.replace('<a href="/blogs.html" class="mobile-nav-item">Blogs</a>', '')
    content = content.replace('<a href="blogs.html" class="mobile-nav-item">Blogs</a>', '')
    content = content.replace('<a href="./blogs.html" class="mobile-nav-item">Blogs</a>', '')

    # Mobile link style B
    content = content.replace('<a class="mobile-nav-item" href="/blogs.html">Blogs</a>', '')
    content = content.replace('<a class="mobile-nav-item" href="blogs.html">Blogs</a>', '')
    content = content.replace('<a class="mobile-nav-item" href="./blogs.html">Blogs</a>', '')

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Removed Blogs menu item from: {filepath}")
