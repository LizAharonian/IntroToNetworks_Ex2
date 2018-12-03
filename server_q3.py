import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '0.0.0.0'
    server_port = 12345
    server.bind((server_ip, server_port))
    server.listen(5)
    while True:
        client_socket, client_address = server.accept()
        print 'Connection from: ', client_address
        data = client_socket.recv(1024)
        while not data == '':
            print 'Received: ', data
            #client_socket.send(data.upper())
            data = client_socket.recv(1024)
        print 'Client disconnected'
        client_socket.close()

def get_file_name_from_message(msg):
    msg = msg.strip("GET")
    msg = msg.strip("\n").strip("HTTP/1.1")
    file_name = msg.strip()
    return file_name

if __name__ == "__main__":
    main()