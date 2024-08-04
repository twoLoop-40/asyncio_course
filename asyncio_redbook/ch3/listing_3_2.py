import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'Connection from {client_address}')

    buffer = b''

    while buffer[-2:] != b'\r\n':
        data = connection.recv(4)
        if not data:
            break
        else:
            print(f'data coming: {data=}')
            buffer = buffer + data

    print(f'All the data is: {buffer=}')

finally:
    server_socket.close()
