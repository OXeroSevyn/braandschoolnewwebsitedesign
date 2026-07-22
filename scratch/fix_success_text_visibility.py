import os

root_dir = r"c:\Subham\aiappsnew\Braand School (Website)"

files_to_fix = [
    "index.html",
    "course.html",
    "courses/index.html"
]

for filename in files_to_fix:
    file_path = os.path.join(root_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        
        # Replace the dark h3 text color with white
        old_h3 = 'style="color: #000; margin-bottom: 10px;">Application Received!</h3>'
        new_h3 = 'style="color: #fff; margin-bottom: 10px;">Application Received!</h3>'
        if old_h3 in content:
            content = content.replace(old_h3, new_h3)
            modified = True
            
        # Replace the dark paragraph text color with semi-transparent white
        old_p = 'style="color: rgba(0,0,0,0.6);">We\'ll get back to you on WhatsApp within 24 hours.</p>'
        new_p = 'style="color: rgba(255,255,255,0.7);">We\'ll get back to you on WhatsApp within 24 hours.</p>'
        if old_p in content:
            content = content.replace(old_p, new_p)
            modified = True
            
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed success text visibility in: {filename}")
        else:
            print(f"No changes made to: {filename}")

print("Done!")
