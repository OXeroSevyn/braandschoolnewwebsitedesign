import urllib.request

pages = [
    ('/', 'Homepage'),
    ('/course/graphic-design-course-siliguri', 'Graphic Design Course'),
    ('/course/ai-for-everyone-siliguri', 'AI for Everyone'),
    ('/course/ar-vr-course-siliguri', 'AR/VR Course'),
    ('/course/digital-marketing-course-siliguri', 'Digital Marketing Course'),
    ('/course/the-ui-ux-design-course-siliguri', 'UI/UX Course'),
    ('/course/the-digital-art-course-siliguri', 'Digital Art Course'),
    ('/course/video-motion-course-siliguri', 'Video Editing Course'),
    ('/gallery', 'Gallery'),
    ('/contact', 'Contact'),
    ('/2025-batch', '2025 Batch'),
]

print('Testing pages...')
all_ok = True
for path, name in pages:
    try:
        url = f'http://localhost:8080{path}'
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=5) as r:
            body = r.read().decode('utf-8', errors='replace')
            status = r.status
            print(f'  [OK {status}] {name}')
    except Exception as e:
        print(f'  [ERR] {name}: {e}')
        all_ok = False

print()
if all_ok:
    print('All pages OK!')
else:
    print('Some pages failed — see above.')
