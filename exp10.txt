from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class LabServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            html = """
            <html>
            <body>
                <h2>Wireshark Clear-Text Lab</h2>
                <form method="POST" action="/login">
                    Username:<br>
                    <input type="text" name="username"><br><br>
                    Password:<br>
                    <input type="password" name="password"><br><br>
                    <input type="submit" value="Login">
                </form>
            </body>
            </html>
            """
            
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

    def do_POST(self):
        if self.path == "/login":
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length).decode()
            
            print("\nReceived login data:")
            print(data)
            
            response = "<h2>Login received</h2><p>Laboratory test completed.</p>"
            
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(response.encode())

server = HTTPServer(("127.0.0.1", 8000), LabServer)

print("Wireshark laboratory server running...")
print("Open: http://127.0.0.1:8000")

server.serve_forever()
