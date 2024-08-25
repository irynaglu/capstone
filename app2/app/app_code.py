from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {PORT}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()