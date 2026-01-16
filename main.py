from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        message = ("안녕하세요! 만나서 반갑습니다!")
        self.wfile.write(message.encode('UTF-8'))

        print("---요청원문---")
        print(self.requestline)
        print(self.headers)

host = 'localhost'
port = 8000



server = HTTPServer((host,port),MyHandler)

print(f"서버가 시작되었습니다! http://{host}:{port}로 접속 가능")
print("종료하려면 터미널에서 Ctrl+C를 누르세요.")

try: 
    server.serve_forever()
except KeyboardInterrupt:
    print("\n서버를 종료합니다.")
    server.server_close()