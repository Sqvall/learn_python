import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
print('Port: 8888 is bind')
sock.listen(5)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client, addr = sock.accept()
result = client.recv(1024)
client.send(b'All ok, message received')
client.close()
sock.close()

print('Message:', result.decode('UTF-8'))
