import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# sock.setblocking(True)
# sock.settimeout(5)
# sock.settimeout(0)  # -> sock.setblocking(False)
sock.settimeout(None)  # -> sock.setblocking(True)

try:
    client, addr = sock.accept()
except socket.error:
    print('No client')
# except socket.timeout:
#     print('time out')
except KeyboardInterrupt:
    print('Socket close')
    sock.close()
else:
    result = client.recv(1024)
    client.close()
    print('Message: ', result.decode('UTF-8'))
