import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip, server_port))
server.listen(5)
while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    concat_client_messages = ""
    data = client_socket.recv(1024)
    concat_client_messages += data
    sent_flag = False
    while not data == '':
        print 'Received: ', data
        data = client_socket.recv(1024)
        concat_client_messages += data
        if len(concat_client_messages) == 22 and not sent_flag:
            client_socket.send('B')
            sent_flag = True

    print 'Client disconnected'
    client_socket.close()