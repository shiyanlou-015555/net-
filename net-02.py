import socket
# 客户端
def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = "你好"
    data = text.encode()
    sock.sendto(data,("127.0.0.1",7855))
    data,addr = sock.recvfrom(200)
    data = data.decode()
    print(data)

if __name__ == '__main__':
    clientFunc()