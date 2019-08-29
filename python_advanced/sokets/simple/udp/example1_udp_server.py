import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 8888))
    result = sock.recv(1024)
    print('Message: ', result.decode('UTF-8'))
    sock.close()


while True:
    main()
