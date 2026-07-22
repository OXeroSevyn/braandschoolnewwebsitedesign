import os
import re
import shutil

# Define mapping of files and target subdirectories
courses = {
    "braanding-course.html": {
        "dir": "brand-design",
        "shapes": [
            "bento_shape_1.png",
            "bento_shape_2.png",
            "bento_shape_3.png",
            "bento_shape_4.png"
        ],
        "hero": "hero_brand.png"
    },
    "creator-course.html": {
        "dir": "content-video",
        "shapes": [
            "creator_shape_1.png",
            "creator_shape_2.png",
            "creator_shape_3.png",
            "creator_shape_4.png"
        ],
        "hero": "hero_creator_inverted.png"
    },
    "business-marketing-course.html": {
        "dir": "business-marketing",
        "shapes": [
            "business_shape_1.png",
            "business_shape_2.png",
            "business_shape_3.png",
            "business_shape_4.png"
        ],
        "hero": "hero_business.png"
    }
}

base_images_dir = "images"
courses_dest_parent = os.path.join(base_images_dir, "courses")

def copy_file_safe(src, dst):
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Copied: {src} -> {dst}")
    else:
        print(f"Warning: Source not found: {src}")

for html_file, config in courses.items():
    print(f"\nProcessing {html_file}...")
    course_dir_name = config["dir"]
    course_dest_dir = os.path.join(courses_dest_parent, course_dir_name)
    
    # Read HTML content
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all referenced image files under images/
    pattern = re.compile(r'images/[a-zA-Z0-9_\-\.\/]+')
    matches = set(pattern.findall(content))
    
    # Sort matches by length descending to replace longer paths first (prevent partial matches)
    sorted_matches = sorted(list(matches), key=lambda x: len(x), reverse=True)
    
    new_content = content
    
    for match in sorted_matches:
        # Ignore "images/all" if it is just a prefix or generic matching
        if match == "images/all":
            continue
            
        # Get path relative to images/ folder
        rel_path = match.replace("images/", "", 1)
        
        # Source path on disk
        src_path = os.path.join(base_images_dir, rel_path)
        
        # Destination path on disk
        dst_path = os.path.join(course_dest_dir, rel_path)
        
        # Copy the image file to the new course-specific directory
        copy_file_safe(src_path, dst_path)
        
        # Replace the path in the HTML file content
        new_match = f"images/courses/{course_dir_name}/{rel_path}"
        new_content = new_content.replace(match, new_match)
        print(f"  Replaced: '{match}' -> '{new_match}'")
        
    # Write updated HTML file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {html_file} successfully.")

print("\nImage organization completed.")
