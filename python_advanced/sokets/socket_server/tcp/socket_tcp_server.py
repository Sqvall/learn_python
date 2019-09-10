import socketserver


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # print(self.request)
        data = self.request.recv(1024).strip()
        print(f'Address: {self.client_address[0]}:{self.client_address[1]}')
        print(f'Data: {data.decode()}')
        self.request.sendall(b'Message received, all OK')


if __name__ == '__main__':
    with socketserver.TCPServer(('0', 8888), EchoTCPHandler) as server:
        server.serve_forever()
