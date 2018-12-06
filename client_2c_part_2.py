"""
UDP client of question 2.c part 2
"""
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
dest_ip = '127.0.0.1'
dest_port = 12345
# send two "A" messages to the server 11 times
for i in range(11):
    msg = "A"
    s.sendto(msg, (dest_ip,dest_port))
    s.sendto(msg, (dest_ip,dest_port))
# receive message from the server
data, sender_info = s.recvfrom(2048)
print "Server sent: ", data
# close client socket
s.close()