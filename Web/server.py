from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleLoginHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read and parse form data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        data = urllib.parse.parse_qs(post_data)

        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        # Simple logic to check login
        if username == "admin" and password == "password":
            message = "Login Succeed"
        else:
            message = "Invalid username or password"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_GET(self):
        try:
            with open("login.html", "rb") as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self.send_error(404, "File Not Found")

# Run the server
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleLoginHandler)
print("Server running at http://localhost:8000")
httpd.serve_forever()
