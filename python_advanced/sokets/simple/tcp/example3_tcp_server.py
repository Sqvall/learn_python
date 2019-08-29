import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8889))
sock.listen(5)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        print('\nSocket CLOSE')
        break
    else:
        print(sock)
        print(client)
        result = client.recv(1024)
        client.close()
        print('Message: ', result.decode('UTF-8'))