import socket
import os.path

# response messages
FILE_FOUND_MSG = "HTTP/1.1 200 OK"
FILE_NOT_FOUND_MSG = "HTTP/1.1 404 Not Found"
REDIRECT_MSG = "HTTP/1.1 301 Moved Permanently"
CLOSE_MSG = "Connection: close"
REDIRECT_CONTENT = "REDIRECT"

# connection settings
IP = '0.0.0.0'
PORT = 12345
MAX_CLIENTS = 5

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = IP
    server_port = PORT
    server.bind((server_ip, server_port))
    server.listen(MAX_CLIENTS)
    while True:
        client_socket, client_address = server.accept()
        print 'Connection from: ', client_address
        data = client_socket.recv(4096)
        #while not data == '':
        print 'Received: ', data
        data = data.split("\r\n")
        # data[0] is the GET line
        file_name = get_file_name_from_message(data[0])
        file_content = get_file_content(file_name)
        # create response for the client request
        response = create_response(file_content)
        client_socket.send(response)
        print 'Client disconnected'
        client_socket.close()

def get_file_name_from_message(msg):
    file_name = msg.split(" ")[1]
    return file_name

def get_file_content(file_name):
    file_to_read = file_name
    # "/" means index.html files in the root folder
    if file_name == "/":
        file_to_read = "files/index.html"
    elif file_name == "/redirect":
        return REDIRECT_CONTENT
    else:
        file_to_read = "files/" + file_name
    # file doesn't exists
    if not os.path.isfile(file_to_read):
        return None
    if file_to_read.endswith(".jpg"):
        file = open(file_to_read, "rb")
    else:
        file = open(file_to_read, "r")
    content = file.read()
    file.close()
    return content

def create_response(file_content):
    response = ""
    if file_content == None:
        response = "{}\r\n {}".format(FILE_NOT_FOUND_MSG, CLOSE_MSG)
    elif file_content == REDIRECT_CONTENT:
        response = "{}\r\n{}Location: /result.html\r\n\r\n".format(REDIRECT_MSG, CLOSE_MSG)
    else:
        response =  "{}\r\n {}\r\n\r\n{}".format(FILE_FOUND_MSG, CLOSE_MSG, file_content)
    return response


if __name__ == "__main__":
    main()