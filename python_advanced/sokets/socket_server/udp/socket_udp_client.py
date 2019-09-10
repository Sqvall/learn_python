import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Hello socket server!', ('localhost', 8888))
result = sock.recv(1024)
print(result.decode('UTF-8'))
