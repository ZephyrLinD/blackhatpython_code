import socket

target_host = "127.0.0.1"
target_port = 80

# build a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data by sendto()
client.sendto("AAABBBCCC", (target_host, target_port))
# UDP don't use to be connect()

# get some data
data, addr = client.recvfrom(4096)

print(data)
