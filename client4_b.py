from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
dest_ip = '127.0.0.1'

dest_port = 12345
for i in range(11):
    msg = "A"
    s.sendto(msg, (dest_ip,dest_port))
    s.sendto(msg, (dest_ip,dest_port))
data, sender_info = s.recvfrom(2048)
print "Server sent: ", data
s.close()