from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"TCP Packet: Source IP {ip_src}:{sport}, Destination IP {ip_dst}:{dport}")

        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"UDP Packet: Source IP {ip_src}:{sport}, Destination IP {ip_dst}:{dport}")

        else:
            print(f"Other Packet: Source IP {ip_src}, Destination IP {ip_dst}, Protocol: {proto}")

print("Starting packet capture...")
sniff(prn=packet_callback, count=10)
