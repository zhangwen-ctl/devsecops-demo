import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


APP_NAME = "devsecops-demo"
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._json(200, {"status": "UP", "service": APP_NAME})
        elif self.path == "/version":
            self._json(200, {"service": APP_NAME, "version": APP_VERSION})
        else:
            self._json(404, {"error": "not found"})

    def _json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def run():
    port = int(os.getenv("PORT", "8080"))
    server = ThreadingHTTPServer(("0.0.0.0", port), RequestHandler)
    print(f"{APP_NAME} listening on port {port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    run()