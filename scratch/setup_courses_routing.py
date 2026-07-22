import os
import glob

base_dir = '/Users/isharoka/Downloads/MAin website'

# 1. Rename courses.html back to course.html
courses_file = os.path.join(base_dir, 'courses.html')
course_file = os.path.join(base_dir, 'course.html')

if os.path.exists(courses_file):
    os.rename(courses_file, course_file)
    print(f"Renamed {courses_file} back to {course_file}")

# 2. Edit .htaccess
htaccess_path = os.path.join(base_dir, '.htaccess')
if os.path.exists(htaccess_path):
    with open(htaccess_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # We want to insert the courses rewrite rule after the contact-us rewrite rule
    new_lines = []
    rule_added = False
    for line in lines:
        new_lines.append(line)
        if 'RewriteRule ^contact-us/?$ /contact.html' in line and not rule_added:
            new_lines.append('RewriteRule ^courses/?$ /course.html [L,NC]\n')
            rule_added = True
            
    with open(htaccess_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Added RewriteRule to .htaccess")

# 3. Edit dev_server.py
dev_server_path = os.path.join(base_dir, 'dev_server.py')
if os.path.exists(dev_server_path):
    with open(dev_server_path, 'r', encoding='utf-8') as f:
        dev_content = f.read()
        
    target_pattern = """        # Rewrite contact page URL variants to contact.html
        if parsed.path in ("/contact", "/contact.html", "/contact/", "/contact-us", "/contact-us/"):
            self.path = "/contact.html" + (f"?{parsed.query}" if parsed.query else "")
            parsed = urllib.parse.urlparse(self.path)"""
            
    replacement_pattern = """        # Rewrite contact page URL variants to contact.html
        if parsed.path in ("/contact", "/contact.html", "/contact/", "/contact-us", "/contact-us/"):
            self.path = "/contact.html" + (f"?{parsed.query}" if parsed.query else "")
            parsed = urllib.parse.urlparse(self.path)
            
        # Rewrite courses URL variants to course.html
        if parsed.path in ("/courses", "/courses/", "/courses.html"):
            self.path = "/course.html" + (f"?{parsed.query}" if parsed.query else "")
            parsed = urllib.parse.urlparse(self.path)"""
            
    new_dev_content = dev_content.replace(target_pattern, replacement_pattern)
    with open(dev_server_path, 'w', encoding='utf-8') as f:
        f.write(new_dev_content)
    print("Updated dev_server.py routing")

# 4. Update references in HTML files to point to '/courses'
html_files = glob.glob(os.path.join(base_dir, '**/*.html'), recursive=True)

for file_path in html_files:
    if 'scratch' in file_path:
        continue
        
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Replace references to /courses.html with /courses
    updated_content = content.replace('/courses.html', '/courses')
    updated_content = updated_content.replace('href="courses.html"', 'href="/courses"')
    updated_content = updated_content.replace("href='courses.html'", "href='/courses'")
    
    # Just in case some /course.html remain, replace them with /courses too
    updated_content = updated_content.replace('/course.html', '/courses')
    updated_content = updated_content.replace('href="course.html"', 'href="/courses"')
    updated_content = updated_content.replace("href='course.html'", "href='/courses'")
    
    if content != updated_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Updated references to /courses in: {file_path}")
