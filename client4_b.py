import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '10.0.2.2'
dest_port = 12345
s.connect((dest_ip, dest_port))
for i in range(11):
    msg = "A"
    s.send(msg)
    s.send(msg)
data = s.recv(4096)
print "Server sent: ", data
s.close()