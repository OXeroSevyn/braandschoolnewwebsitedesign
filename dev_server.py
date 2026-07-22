import http.server
import socketserver
import os
import sys
import json
import urllib.parse
import urllib.request
import base64
import time

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
GALLERY_CACHE_TTL_SEC = 5
_gallery_manifest_cache = {"expires": 0.0, "payload": None}

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/submit":
            self._handle_api_submit()
            return
        self.send_error(404, "Not Found")

    def _handle_api_submit(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Decodes the Discord Webhook URL securely on the server
            encoded = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTQ4OTI4MTM3MzIzNDY1OTMzOC9ZazJ2WkJFUUpqRVYycEdwR045Z05uUzVRaDFBcml4OVNaSk0tSUltVnNvZ0Zpc1d5c0lGMHQyMTlTbkI3NW9kMGRsUQ=="
            webhook_url = base64.b64decode(encoded).decode('utf-8')
            
            # Forward the payload to Discord
            req = urllib.request.Request(
                webhook_url,
                data=post_data,
                headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as response:
                response.read()
                
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b'{"success":true}')
        except Exception as e:
            try:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
            except Exception:
                pass

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # Rewrite legacy category paths to the flat /blogs/ directory
        for prefix in ("/podcast/", "/siliguri/", "/blog/siliguri-blog/"):
            if parsed.path.startswith(prefix):
                new_path = parsed.path.replace(prefix, "/blogs/", 1)
                self.path = new_path + (f"?{parsed.query}" if parsed.query else "")
                parsed = urllib.parse.urlparse(self.path)
                break
        
        if parsed.path.startswith("/blog/") and not parsed.path.startswith(("/blog/siliguri-blog/", "/blogs/")):
            slug = parsed.path[len("/blog/"):]
            if slug.strip("/") and slug != "index.html" and not slug.startswith("page/"):
                new_path = "/blogs/" + slug
                self.path = new_path + (f"?{parsed.query}" if parsed.query else "")
                parsed = urllib.parse.urlparse(self.path)
                
        # Rewrite contact page URL variants to contact.html
        if parsed.path in ("/contact", "/contact.html", "/contact/", "/contact-us", "/contact-us/"):
            self.path = "/contact.html" + (f"?{parsed.query}" if parsed.query else "")
            parsed = urllib.parse.urlparse(self.path)
            
        # Rewrite courses URL variants to course.html
        if parsed.path in ("/courses", "/courses/", "/courses.html"):
            self.path = "/courses.html" + (f"?{parsed.query}" if parsed.query else "")
            parsed = urllib.parse.urlparse(self.path)
            
        # Rewrite virtual asset paths under /course/ or /courses/ to point to actual root directories
        if parsed.path.startswith(("/course/assets/", "/course/images/", "/course/uploads/", "/courses/assets/", "/courses/images/", "/courses/uploads/")):
            new_path = parsed.path.replace("/courses/", "/", 1) if parsed.path.startswith("/courses/") else parsed.path.replace("/course/", "/", 1)
            self.path = new_path + (f"?{parsed.query}" if parsed.query else "")
            parsed = urllib.parse.urlparse(self.path)
            
        # Rewrite virtual course page URLs to physical HTML files in the root
        elif parsed.path.startswith("/courses/") and parsed.path not in ("/courses/", "/courses.html"):
            course_name = parsed.path[len("/courses/"):]
            if course_name.endswith(".html"):
                course_name = course_name[:-5]
            
            # Map video-motion to video-editing
            if "video-motion" in course_name:
                course_name = course_name.replace("video-motion", "video-editing")
            
            # If the specific -siliguri file doesn't exist, fallback to the generic course file
            test_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "courses", f"{course_name}.html")
            if not os.path.exists(test_path) and course_name.endswith("-siliguri"):
                course_name = course_name[:-9]
                
            self.path = f"/courses/{course_name}.html" + (f"?{parsed.query}" if parsed.query else "")
            parsed = urllib.parse.urlparse(self.path)

        # Local dev helper: emulate the production PHP gallery scanner endpoint.
        # This keeps life-at-bs.html working even though this server cannot execute PHP.
        if parsed.path in ("/uploads/life-at-bs/list.php", "/uploads/life-at-bs/list.json"):
            self._serve_life_at_bs_gallery_list()
            return

        path = self.translate_path(self.path)
        if os.path.isdir(path):
            super().do_GET()
            return
        if not os.path.exists(path) and not os.path.splitext(path.rstrip("/"))[1]:
            clean_path = path.rstrip("/")
            html_path = clean_path + ".html"
            if os.path.exists(html_path):
                # Update self.path to map to the html file, keeping any query string if present
                parsed_path = urllib.parse.urlparse(self.path)
                self.path = parsed_path.path.rstrip("/") + ".html" + (f"?{parsed_path.query}" if parsed_path.query else "")
                path = html_path

        if os.path.isfile(path) and "Range" in self.headers:
            self._serve_range_request(path)
            return

        super().do_GET()

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()

    def _serve_range_request(self, path):
        range_header = self.headers.get("Range", "")
        if not range_header.startswith("bytes="):
            self.send_error(400, "Bad Range Request")
            return

        size = os.path.getsize(path)
        range_val = range_header.split("=")[1].strip()
        if "," in range_val:
            self.send_error(501, "Multiple ranges not supported")
            return

        start = 0
        end = size - 1
        parts = range_val.split("-")
        if len(parts) != 2:
            self.send_error(400, "Bad Range Request")
            return

        start_str = parts[0].strip()
        end_str = parts[1].strip()

        try:
            if not start_str and end_str:
                start = size - int(end_str)
            elif start_str and not end_str:
                start = int(start_str)
            elif start_str and end_str:
                start = int(start_str)
                end = int(end_str)
        except ValueError:
            self.send_error(400, "Bad Range Request")
            return

        if start < 0:
            start = 0
        if end >= size:
            end = size - 1

        if start > end:
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return

        try:
            with open(path, "rb") as f:
                self.send_response(206)
                self.send_header("Content-Type", self.guess_type(path))
                self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
                self.send_header("Content-Length", str(end - start + 1))
                self.end_headers()
                
                f.seek(start)
                left = end - start + 1
                chunk_size = 64 * 1024
                while left > 0:
                    chunk = f.read(min(chunk_size, left))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    left -= len(chunk)
        except (ConnectionResetError, ConnectionAbortedError):
            pass
        except Exception as e:
            try:
                self.send_error(500, f"Internal Server Error: {str(e)}")
            except Exception:
                pass

    def _serve_life_at_bs_gallery_list(self):
        now = time.time()
        cached = _gallery_manifest_cache
        if cached["payload"] is not None and now < cached["expires"]:
            payload = cached["payload"]
        else:
            uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads", "life-at-bs")
            allowed_extensions = {
                # Images
                "webp", "jpg", "jpeg", "png", "gif", "avif", "svg",
                # Videos
                "mp4", "webm",
            }
            video_extensions = {"mp4", "webm"}

            files = []
            if os.path.isdir(uploads_dir):
                for name in os.listdir(uploads_dir):
                    if name.startswith("."):
                        continue
                    full_path = os.path.join(uploads_dir, name)
                    if os.path.isdir(full_path):
                        continue
                    if name in ("list.php", "list.json"):
                        continue

                    ext = os.path.splitext(name)[1].lstrip(".").lower()
                    if ext not in allowed_extensions:
                        continue

                    stat = os.stat(full_path)
                    files.append({
                        "name": name,
                        "type": "video" if ext in video_extensions else "image",
                        "size": stat.st_size,
                        "modified": int(stat.st_mtime),
                    })

            files.sort(key=lambda f: f.get("modified", 0), reverse=True)
            payload = json.dumps(files, separators=(",", ":")).encode("utf-8")
            cached["payload"] = payload
            cached["expires"] = now + GALLERY_CACHE_TTL_SEC

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "public, max-age=60")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Serving Braand School at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        sys.exit(0)
