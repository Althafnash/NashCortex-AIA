import socket
from datetime import datetime

def run(): 
    net = input("Enter the IP address: ")
    addr = input('Enter Addr')
    net1 = net.split('.')
    a = '.'

    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = int(input("Enter the Starting PORT Number: "))
    en1 = int(input("Enter the Last PORT Number: "))
    en1 = en1 + 1
    t1 = datetime.now()

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr,135))
    if result == 0:
        return 1
    else :
        return 0

    for ip in range(st1,en1):
        addr = net2 + str(ip)
        if (scan(addr)):
            print (addr , "is live")

    t2 = datetime.now()
    total = t2 - t1
    print ("Scanning completed in: " , total)