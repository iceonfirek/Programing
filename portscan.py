import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("请输入IP: ")
port = int(input("请输入端口: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")


portScanner(port)
