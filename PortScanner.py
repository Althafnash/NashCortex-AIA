import socket
from socket import *
from datetime import datetime
import time

def port_scanner():
    try:
        target = input("Enter the target IP address: ")
        ip = socket.gethostbyname(target)

        print(f"Scanning the target {ip}")
        print(f"Time started: {datetime.now()}")

        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} : open")
            sock.close()
    except socket.gaierror:
        print("Host cannot be resolved")
    except socket.error:
        print("Could not connect to the server")

def Live_port_scanner():
    startTime = time.time()
    target = input('Enter the host to be scan: ')
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
    
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()
    print('Time taken:', time.time() - startTime)

def Detailed_port_scanner():
    try:
        target = input("Enter the target IP address: ")
        port = input("Enter the port number to scan : ")
        port = int(port)
        ip = socket.gethostbyname(target)

        print(f"Scanning the target {ip}")
        print(f"Time started: {datetime.now()}")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} : open")
        else:
            print(f"{port} not found")
        sock.close()
    except socket.gaierror:
        print("Host cannot be resolved")
    except socket.error:
        print("Could not connect to the server")