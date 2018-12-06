"""
TCP client of question 2.b
"""
import socket
from time import sleep

def send_messages():
    """
    send two "A" messages to the server.
    """
    msg = 'A'
    s.send(msg)
    s.send(msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server IP and port
dest_ip = '127.0.0.1'
dest_port = 12345
s.connect((dest_ip, dest_port))
print "client sent message to server"
send_messages()
sleep(0.2)
# client sends 10 more pairs of "A" messages
for i in range(10):
    send_messages()
# receive message from the server
data = s.recv(4096)
print "Server sent: ", data
# close client socket
s.close()


