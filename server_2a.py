"""
TCP server of question 2.a
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
    concat_client_messages = ""
    # get message from the client
    data = client_socket.recv(15000)
    while not data == '':
        print 'Received: ', data
        concat_client_messages += data
        # wait until client sends 15000 long message before sending response
        if len(concat_client_messages) == 15000:
            # send response to the client
            client_socket.send('B')
        data = client_socket.recv(15000)
    print 'Client disconnected'
    # close client socket
    client_socket.close()