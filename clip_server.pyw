from http.server import HTTPServer, BaseHTTPRequestHandler
import pyperclip

HOST = "0.0.0.0"
PORT = 8765

class ClipboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/clip":
            text = pyperclip.paste()
            data = text.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/clip":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            pyperclip.copy(body)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Undertryck standardloggar

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), ClipboardHandler)
    print(f"Urklippsserver körs på port {PORT}...")
    server.serve_forever()