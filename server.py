from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open('templates/contacts.html', 'r', encoding='utf-8') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()
#1
