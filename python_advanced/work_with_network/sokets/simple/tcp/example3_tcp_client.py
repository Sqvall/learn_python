import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8887))
sock.send(b'Test message')
sock.close()
