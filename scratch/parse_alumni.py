import re
import json
import os
from html.parser import HTMLParser

class StudentAlumniParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.students = []
        self.current_student = None
        self.in_heading = False
        self.heading_level = None
        self.heading_text = ""
        self.in_info_list = False
        self.current_li_type = None
        self.in_info_text = False
        self.info_text_content = ""
        self.in_anchor = False
        self.anchor_href = ""
        self.anchor_text = ""
        self.current_links = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Detect new student section
        # The image widget contains the student picture. Let's look for images inside column-50 or images that look like student photos.
        if tag == "img":
            src = attrs_dict.get("src", "")
            # Verify if it's a student picture (usually under wp-content/uploads/2026/01/ or Ankita-Basnet.webp)
            if "/uploads/" in src and not src.endswith("cropped-bs-logo-32x32.png") and not src.endswith("logo-1-e1687611356217-800x357.png"):
                # Save previous student if complete
                if self.current_student:
                    self.students.append(self.current_student)
                self.current_student = {
                    "name": "",
                    "role": "",
                    "image": src,
                    "course": "",
                    "location": "",
                    "links": []
                }
                self.current_links = []

        # Detect heading tags (for Name and Role)
        if self.current_student and tag in ["h2", "div"] and "class" in attrs_dict:
            classes = attrs_dict.get("class", "")
            if "elementor-heading-title" in classes:
                self.in_heading = True
                self.heading_level = tag
                self.heading_text = ""

        # Detect list item elements for Course, Location, and Portfolio links
        if self.current_student and tag == "li":
            # We look for structured items in the lists
            pass

        if self.current_student and tag == "div" and "class" in attrs_dict:
            if "onovo-text" in attrs_dict["class"]:
                self.in_info_text = True
                self.info_text_content = ""

        if self.current_student and tag == "a" and self.in_info_text:
            self.in_anchor = True
            self.anchor_href = attrs_dict.get("href", "")
            self.anchor_text = ""

    def handle_endtag(self, tag):
        if self.in_heading:
            if tag == self.heading_level:
                self.in_heading = False
                val = self.heading_text.strip()
                if val:
                    if not self.current_student["name"]:
                        self.current_student["name"] = val
                    elif not self.current_student["role"]:
                        self.current_student["role"] = val

        if self.in_anchor:
            if tag == "a":
                self.in_anchor = False
                self.current_links.append({
                    "label": self.anchor_text.strip(),
                    "url": self.anchor_href
                })

        if self.in_info_text:
            if tag == "div":
                self.in_info_text = False
                val = self.info_text_content.strip()
                # If we parsed anchor tags, these are links.
                if self.current_links:
                    self.current_student["links"] = list(self.current_links)
                    self.current_links = []
                else:
                    # Let's decide if this is course or location based on content or heuristics
                    # Let's clean up linebreaks
                    lines = [l.strip() for l in val.split("\n") if l.strip()]
                    cleaned_val = " ".join(lines)
                    
                    if not self.current_student["course"] and ("Course" in cleaned_val or "Design" in cleaned_val or "Marketing" in cleaned_val or "Editing" in cleaned_val or "Branding" in cleaned_val or "UX" in cleaned_val):
                        self.current_student["course"] = cleaned_val.replace("Course:", "").strip()
                    elif not self.current_student["location"]:
                        self.current_student["location"] = cleaned_val.replace("Location:", "").strip()

    def handle_data(self, data):
        if self.in_heading:
            self.heading_text += data
        if self.in_anchor:
            self.anchor_text += data
        elif self.in_info_text:
            self.info_text_content += data

    def close(self):
        super().close()
        if self.current_student:
            self.students.append(self.current_student)

def clean_parsed_data(students):
    # Some cleaning logic for student records
    cleaned = []
    for s in students:
        if not s["name"]:
            continue
        # Deduplicate and clean up fields
        s["name"] = s["name"].strip()
        s["role"] = s["role"].strip()
        
        # Heuristics for course/location
        # Let's clean up if both fields got mixed
        course = s["course"]
        location = s["location"]
        
        # Course cleanup
        course_match = re.search(r'(Branding Course|Graphic Design|Digital Marketing|Video Editor|Content Creation|Motion|UI/UX)', course, re.I)
        if course_match:
            s["course"] = course_match.group(0)
            
        cleaned.append(s)
    return cleaned

with open(r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\student-alumni.html", "r", encoding="utf-8") as f:
    html_content = f.read()

parser = StudentAlumniParser()
parser.feed(html_content)
parser.close()

cleaned_students = clean_parsed_data(parser.students)

# Let's print the count and first few records
print(f"Total students parsed: {len(cleaned_students)}")

# Save to JSON for verification
with open(r"c:\Subham\aiappsnew\Braand School (Website 2.0)\Braand school version 1.0\Braand school version 1.0\scratch\parsed_students.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_students, f, indent=2)
print("Saved to scratch/parsed_students.json")
