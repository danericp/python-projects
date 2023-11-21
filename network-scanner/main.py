
print("Importing the Python module for enabling network scanning")
import scapy.all as scapy

str_ip = "192.168.1.1"

def do_scan_ip(str_ip):
    # Get a summary of ARP request
    arp_request = scapy.ARP(pdst=str_ip)
    # arp_request.pdst=str_ip
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.dst="ff:ff:ff:ff:ff:ff"
    # scapy.ls(broadcast)
    print(broadcast.summary())
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()

do_scan_ip(str_ip)