import socket

target_host = "www.baidu.com"
target_port = 80

# Build a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_IENT means that we will use a standard IPv4 address or Server name
# SOCK_STREAM means that this is a TCP clent

# connect client
client.connect((target_host, target_port))

# send some datas
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

# get the datas
response = client.recv(4096)

print(response)
