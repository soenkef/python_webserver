from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)

        self.wfile.write("Hallo Welt".encode())


address = ("127.0.0.1", 10080)

server = HTTPServer(address, MyRequestHandler)
server.serve_forever()