import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '10.0.2.2'
dest_port = 12345
s.connect((dest_ip, dest_port))
msg = "A" * 15000
s.send(msg)
data = s.recv(4096)
print "Server sent: ", data
s.close()