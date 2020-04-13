import socket
remoteServer = input("enter the port to scan:")

for port in range(1,1001):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServer,port))
    if result ==0:
        print("Port{}:Open".format(port))
    else:
        print("Port{}:Close".format(port))
    sock.close()

