from http.server import HTTPServer, BaseHTTPRequestHandler

# 태그 생성
def maketag(isopen,tagname):
        if isopen:
            return f"<{tagname}>"
        else:
            return f"</{tagname}>"

nametag = ["h1","p","div","script"]
        
h1_content = "매슬로우의 욕구이론 5단계"
bodyh = maketag(True,nametag[0]) + h1_content + maketag(False,nametag[0])

p_content = "1. 생리적 욕구 (Physiological Needs) <br> 인간이 생존하기 위한 가장 기본적인 욕구 "
bodyp = maketag(True,nametag[1]) + p_content + maketag(False,nametag[1])

p_content2 = "2. 안전 욕구 (Safety Needs) <br> 신체적·심리적 안전과 안정에 대한 욕구 "
bodyp2 = maketag(True,nametag[1]) + p_content2 + maketag(False,nametag[1])

p_content3 = "3. 사회적 욕구 / 소속과 사랑의 욕구 (Belongingness and Love Needs) <br> 타인과 관계를 맺고 소속되기를 원하는 욕구 "
bodyp3 = maketag(True,nametag[1]) + p_content3 + maketag(False,nametag[1])

p_content4 = "4. 존중 욕구 (Esteem Needs) <br> 자신과 타인으로부터 인정받고 존중받고자 하는 욕구 "
bodyp4 = maketag(True,nametag[1]) + p_content4 + maketag(False,nametag[1])

p_content5 = "5. 자아실현 욕구 (Self-actualization Needs) <br> 자신의 잠재력을 최대한 발휘하고자 하는 욕구 <br> "
"매슬로우는 하위 욕구가 비교적 충족되어야 상위 욕구로 이동한다고 보았습니다. 즉, 생존이 불안하면 자아실현을 추구하기 어렵다는 관점입니다"
bodyp5 = maketag(True,nametag[1]) + p_content5 + maketag(False,nametag[1])



log_content = "console.log('응답을 받음!!');"
logprint = maketag(True,nametag[3]) + log_content + maketag(False,nametag[3])

#server get 응답 설정
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[Log] 요청 수신: {self.path}")
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(bodyh.encode('UTF-8'))
        self.wfile.write(bodyp.encode('UTF-8'))
        self.wfile.write(bodyp2.encode('UTF-8'))
        self.wfile.write(bodyp3.encode('UTF-8'))
        self.wfile.write(bodyp4.encode('UTF-8'))
        self.wfile.write(bodyp5.encode('UTF-8'))
        self.wfile.write(logprint.encode('UTF-8'))
        print("[Log] 응답 전송 완료")


    
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