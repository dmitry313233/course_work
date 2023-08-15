from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = 'localhost'
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def get_html_content(self):
        return """
        <!doctype html>
<!-- Корень документа -->
<html lang="en">
  <!-- Информация для браузера -->
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">


      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <!-- Заголовок страницы -->
    <title>Hello world</title>
  </head>
  <body>
<div class="container">
    <div class="row mt-3">
        <div class="col-4">
            <div class="card bg-primary">
                <div class="card-body text-white">
                    <h3 class="card-title"> Контактная данные</h3>
                    <div class='row'>
                        <div class="col-6">Москва</div>
                        <div class="col-6">+7 777 7777</div>
                        <div class="col-6">Санкт-Петербург</div>
                        <div class="col-6">+8 888 8888</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-4">
        <div class="card">
  <div class="card-body">
      <h3 class="card-title">Оставьте заявку</h3>
      <form>
  <div class="mb-3">
    <input name='name' type="text" class="form-control" id="exampleInputEmail1" placeholder="Имя">
  </div>
  <div class="mb-3">
    <input name='email' type="email" placeholder="email" class="form-control" id="exampleInputPassword1">
  </div>
      <div class="mb-3">
      <textarea name='message' class="form-control" placeholder="Сообщение" id="exampleFormControlTextarea1" rows="3"></textarea>
  </div>
  <button type="submit" class="btn btn-primary form-control">Отправить</button>
</form>
  </div>
</div>
            </div>
    </div>
</div>
  </body>
</html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.get_html_content()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_content, 'utf-8'))

if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped.')
