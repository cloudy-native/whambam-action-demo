"""A tiny JSON API for the whambam GitHub Action demo: python3 app.py [PORT]."""
import json
import random
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def find_user():
    """Pretend to look the user up: a few milliseconds of work."""
    time.sleep(random.uniform(0.002, 0.004))
    return {"id": 42, "name": "Ada"}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # keep-alive, like a real API

    def do_GET(self):
        body = json.dumps({"user": find_user()}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


class Server(ThreadingHTTPServer):
    daemon_threads = True
    request_queue_size = 256


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"listening on http://127.0.0.1:{port}", flush=True)
    Server(("127.0.0.1", port), Handler).serve_forever()
