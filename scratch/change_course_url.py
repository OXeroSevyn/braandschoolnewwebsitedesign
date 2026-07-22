import os
import re

def update_directory(dir_path):
    for root, dirs, files in os.walk(dir_path):
        # Ignore git, scratch, logs, etc
        if any(ignored in root for ignored in ['.git', 'scratch', 'logs', '__MACOSX']):
            continue
            
        for file in files:
            if file.endswith('.html') or file.endswith('.json') or file == 'htaccess.txt':
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # We want to replace /course/ with /courses/ inside href="", data-href="", and also in action="" or src="" if it exists.
                # Just replacing "/course/" with "/courses/" across all files is mostly safe for this site,
                # as there are no assets named /course/ since they were also renamed or mapped.
                
                # Using a regex to be slightly safer: match any attribute starting with /course/
                # like href="/course/digital-marketing" -> href="/courses/digital-marketing"
                
                new_content = re.sub(r'="/course/', '="/courses/', content)
                new_content = new_content.replace("'/course/", "'/courses/")
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {file_path}")

update_directory('.')
