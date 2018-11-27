import socket

# 服务端编程
def severFuc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#AF_INET代表ipv4，SOCK_DGRAM代表使用UDP通信
    # 127.0.0.1
    addr = ("127.0.0.1",7855)
    sock.bind(addr)
    # 接受对方消息
    data , addr = sock.recvfrom(500)
    print(data)
    print(type(data))
    text = data.decode()
    print(text)
    # 给对方返回消息
    rsp = "hello"
    data = rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    print("消息传输开始")
    severFuc()
    print("消息传输结束")