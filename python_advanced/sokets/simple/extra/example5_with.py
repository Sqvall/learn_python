import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 8888))
    print('Port: 8888 is bind')
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        result = client.recv(1024)
        client.close()
        print('Message: ', result.decode('UTF-8'))
