from socket import socket, AF_INET, SOCK_DGRAM
import sys

def main(argv):
    s = socket(AF_INET, SOCK_DGRAM)
    source_ip = "0.0.0.0"
    source_port = 12345
    s.bind((source_ip, source_port))
    concat_client_messages = ""
    while True:
        data, sender_info = s.recvfrom(15000)
        print("Received: " + data)
        concat_client_messages += data
        if(len(concat_client_messages == 15000)):
            s.sendto("B", sender_info)


if __name__ == "__main__":
	main(sys.argv[1:])
