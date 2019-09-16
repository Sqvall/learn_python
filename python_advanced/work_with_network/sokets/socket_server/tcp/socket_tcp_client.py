import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('0', 8888))
sock.send(b'Hello socket server!')
result = sock.recv(1024)
print(result.decode('UTF-8'))
sock.close()
