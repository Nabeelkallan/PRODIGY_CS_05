# PRODIGY_CS_05

# Packet Sniffer Tool

This is a simple packet sniffer tool written in Python using the Scapy library. The tool captures and analyzes network packets, displaying information such as source and destination IP addresses, protocols, and payload data.

## Features
- Captures TCP and UDP packets.
- Displays source and destination IP addresses and ports.
- Works on both Linux and Windows environments.

## Prerequisites

- Python 3.x
- Scapy library

## Installation

### Linux

1. **Install Python 3** (if not already installed):
   sudo apt update
   sudo apt install python3 python3-pip
   
Install Scapy:
sudo pip3 install scapy

(Optional) Install libpcap: For packet sniffing on Linux, libpcap is recommended for better performance.
sudo apt install libpcap-dev
Run the tool:

Save the Python script as packet_sniffer.py

Run the following command:
sudo python3 packet_sniffer.py

Windows

Install Python 3:

Download and install Python 3 from python.org.
During installation, make sure to check the box to add Python to the system PATH.

Install Scapy: Open cmd or PowerShell and run:
pip install scapy

Install Npcap: Open cmd or PowerShell and run the following command to install Npcap using winget:
winget install Npcap

If you don't have winget installed, download and install Npcap manually from Npcap's official website.

Run the tool:
Save the Python script as packet_sniffer.py

Open cmd and run:
python packet_sniffer.py

Usage
The packet sniffer tool will capture and display information on the first 10 network packets it detects. You can modify the script to capture more or fewer packets as needed.

Example output:
Starting packet capture...
UDP Packet: Source IP 10.0.2.15:48837, Destination IP 192.168.1.1:53
TCP Packet: Source IP 10.0.2.15:54321, Destination IP 192.168.1.1:80
Other Packet: Source IP 10.0.2.15, Destination IP 192.168.1.1, Protocol: 1
Troubleshooting

Linux:
If you're seeing permission issues, ensure that you're running the script with sudo.

Windows:
If you encounter No libpcap provider available errors, ensure Npcap is installed correctly.
If you don't want to install Npcap, you cannot sniff Layer 2 traffic (Ethernet). However, you can modify the script to sniff only Layer 3 traffic using conf.L3socket.
