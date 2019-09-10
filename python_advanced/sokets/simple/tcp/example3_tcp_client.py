import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.sendto(b'TCP client message', ('127.0.0.1', 8888))
result = sock.recv(1024)
print(result.decode('UTF-8'))
sock.close()
