import socket
def tcp_srv():
    # 建立通信
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr = ("127.0.0.1", 8899)
    sock.bind(addr)
    sock.listen()
    # 监听接入访问的socket
    while True:
        #接受访问的元组第一个元素赋值给skt，建立一个通讯的链接通路
        skt,addr = sock.accept()#skt链接水管，可以理解为窗口打开
        #接受对方的发送内容，利用接收到的socket接收内容
        msg = skt.recv(500)
        msg = msg.decode()
        rst = "Received msg: {0} from {1}".format(msg, addr)
        print(rst)
        # 6. 如果有必要，给对方发送反馈信息
        skt.send(rst.encode())

        # 7. 关闭链接通路
        skt.close()


if __name__ == "__main__":
    print("Starting tcp server.......")
    tcp_srv()
    print("Ending tcp server.......")
