"""
TCP client of question 2.a
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server IP and port
dest_ip = '127.0.0.1'
dest_port = 12345
s.connect((dest_ip, dest_port))
# message is the character "A" 15,000 times
msg = 'A' * 15000
# send message to the server
s.send(msg)
print "client sent message to server"
# receive message from the server
data = s.recv(4096)
print "Server sent: ", data
# close client socket
s.close()