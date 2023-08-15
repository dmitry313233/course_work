from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def get_html(self):
        with open('<>home_work.html', encoding='utf-8') as file:
            data = file.read()
            return data

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page = self.get_html()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")