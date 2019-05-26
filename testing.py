from port_scanner import Scanner

#result = Scanner()

for port_number in range(1,54):
    result = Scanner().pscan('8.8.8.8',port_number,'udp')
    print("Port {} is {}".format(port_number,result))
#%%
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('8.8.8.', 53)
message = b'This is our message. It will be sent all at once'