from http.server import HTTPServer, BaseHTTPRequestHandler

# 태그 생성
def maketag(isopen,tagname):
        if isopen:
            return f"<{tagname}>"
        else:
            return f"</{tagname}>"
        
        
head_content = "안녕하세요"
head = maketag(True,"h1") + head_content + maketag(False,"h1")

#server get 응답 설정
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(head.encode('UTF-8'))



    
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