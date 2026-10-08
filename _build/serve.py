"""Local preview server for site/ on port 8765, with Cache-Control: no-store (rule D18).

Run:  python serve.py      then open http://localhost:8765/index.html
"""
import functools
import http.server
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = 8765


class NoStoreHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".webp": "image/webp",
        ".woff2": "font/woff2",
        ".mp4": "video/mp4",
        ".js": "text/javascript",
        ".css": "text/css",
    }

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()


if __name__ == "__main__":
    handler = functools.partial(NoStoreHandler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler) as httpd:
        print(f"Serving {ROOT} at http://localhost:{PORT}/index.html (no-store)")
        httpd.serve_forever()
