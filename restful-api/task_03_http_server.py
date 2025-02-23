#!/usr/bin/python3
# task_03_http_server.py
"""Module to implement simple server using http.server"""

import http.server
import json
from http import HTTPStatus


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """server class"""
    def do_GET(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


if __name__ == '__main__':
    server_address = ("localhost", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
