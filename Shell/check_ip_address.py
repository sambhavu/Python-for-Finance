import socket 

#check if IP Addresses are online
for host in ip_addresses
    print(ping -i 1)
    
socket_obj = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
result = stocket_obj.connect_ex((add,port))
socket_obj.close()

