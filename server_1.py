"""
TCP echo server of question 1
"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip, server_port))
# listen to client connection requests
server.listen(5)
while True:
    # accept client connection request
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    # get message from the client
    data = client_socket.recv(1024)
    while not data == '':
        print 'Received: ', data
        # send message to the client (same message we got with uppercase)
        client_socket.send(data.upper())
        # get message from the client
        data = client_socket.recv(1024)
    print 'Client disconnected'
    # close client socket
    client_socket.close()