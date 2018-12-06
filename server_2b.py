"""
TCP server of question 2.b
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
    data = client_socket.recv(1024)
    concat_client_messages += data
    sent_flag = False
    while not data == '':
        print 'Received: ', data
        # get message from the client
        data = client_socket.recv(1024)
        concat_client_messages += data
        # server sends response after the message length is 22
        if len(concat_client_messages) == 22 and not sent_flag:
            # send response to the client
            client_socket.send('B')
            sent_flag = True

    print 'Client disconnected'
    # close client socket
    client_socket.close()