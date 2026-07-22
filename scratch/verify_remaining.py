import urllib.request

pages = [
    ('/gallery', 'Gallery'),
    ('/contact', 'Contact'),
    ('/2025-batch', '2025 Batch'),
]

for path, name in pages:
    try:
        url = f'http://localhost:8080{path}'
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as r:
            status = r.status
            r.read()   # consume
            print(f'  [OK {status}] {name}')
    except Exception as e:
        print(f'  [ERR] {name}: {e}')
