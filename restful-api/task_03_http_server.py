#!/usr/bin/python3
""" It contains the subclass:
    BaseHTTPRequestHandler """

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that defines responses for various endpoints.

    Endpoints:
    - GET /: Returns a plain text greeting message.
    - GET /data: Returns a JSON object with sample user data.
    - GET /status: Returns a plain text "OK" to indicate server status.
    - GET /info: Returns a JSON object describing the API version and purpose.
    - Any other path: Returns a 404 Not Found with a plain text message.
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.wfile.write(json.dumps(info).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()  # To start the server
