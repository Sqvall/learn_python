import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))


def main():
    while True:
        try:
            result = sock.recv(1024)
        except KeyboardInterrupt:
            sock.close()
            print('\nSocket CLOSE')
            break
        else:
            print('Message: ', result.decode('UTF-8'))


if __name__ == '__main__':
    main()
