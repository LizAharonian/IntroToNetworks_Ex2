"""
UDP client of question 2.c part 1
"""
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
# server IP and port
dest_ip = '127.0.0.1'
dest_port = 12345
msg = "A" * 15000
# send message to the server
s.sendto(msg, (dest_ip,dest_port))
# receive message from the server
data, sender_info = s.recvfrom(2048)
print "Server sent: ", data
# close client socket
s.close()