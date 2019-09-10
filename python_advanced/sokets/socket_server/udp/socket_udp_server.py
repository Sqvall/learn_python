import socketserver


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # print(self.request)
        data, socket = self.request
        print(f'Address: {self.client_address[0]}:{self.client_address[1]}')
        print(f'Data: {data.decode()}')
        socket.sendto(b'Message received, all OK', self.client_address)


if __name__ == '__main__':
    with socketserver.UDPServer(('0', 8888), EchoUDPHandler) as server:
        server.serve_forever()
