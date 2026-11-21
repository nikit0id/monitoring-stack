import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Receiver(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/alerts":
            self.send_error(404)
            return
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        for alert in body["alerts"]:
            print(alert["status"], alert["labels"]["alertname"], flush=True)
        self.send_response(200)
        self.end_headers()


HTTPServer(("", 8080), Receiver).serve_forever()
