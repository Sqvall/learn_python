import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print(f'Address: {self.client_address[0]}')
        print(f'Data: {data.decode()}')
        self.request.sendall(b'Message received, all OK')


if __name__ == '__main__':
    with ThreadingTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
