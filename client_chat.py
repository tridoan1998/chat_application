import socket

client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1', port))

recv_msg = client_socket.recv(1024)
print(recv_msg)

send_msg = input("Enter your user name(prefix with #):")
client_socket.send(send_msg)

while True:
    recv_msg = client_socket.recv(1024)
    print(recv_msg)
    send_msg = input("Send your message in format [@uesr:message] ")
    if send_msg == 'exit':
        break
    else:
        client_socket.send(send_msg)

client_socket.close()


