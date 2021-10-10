import socket, select

port = 12345
socket_list = []
users = {}
server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1 )
server_socket.bind(('', port))
server_socket.listen(5)
socket_list.append(server_socket)
while True:
        ready_to_read, ready_to_write, in_error = select.select(socket_list, [],[], 0)
        for sock in ready_to_read:
            if sock == server_socket:
