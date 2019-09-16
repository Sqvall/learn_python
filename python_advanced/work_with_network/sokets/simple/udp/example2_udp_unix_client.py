import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Hello socket! with file(AF_UNIX)', 'unix.sock')
