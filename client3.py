import socket
from time import sleep

def send_messages():
    msg = 'A'
    s.send(msg)
    s.send(msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '10.0.2.2'

dest_port = 12345
s.connect((dest_ip, dest_port))

print "client sent message to server"
send_messages()
sleep(0.2)
for i in range(10):
    send_messages()

data = s.recv(4096)
print "Server sent: ", data
s.close()


