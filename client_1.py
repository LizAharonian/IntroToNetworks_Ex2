"""
TCP client of question 1
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '127.0.0.1'
dest_port = 12345
s.connect((dest_ip, dest_port))
msg = raw_input("Message to send: ")
# client is not closed until "quit" received
while not msg == 'quit':
    # send message (user input) to the server
    s.send(msg)
    # receive response from the server
    data = s.recv(4096)
    print "Server sent: ", data
    # get message to the server from the user
    msg = raw_input("Message to send: ")
# close client socket
s.close()