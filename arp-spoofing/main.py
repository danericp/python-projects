#!/usr/bin/env python

import scapy.all as scapy

str_ip_ap = "10.0.2.1"
str_ip_target = "10.0.2.7"
str_mac_ap = "52:54:00:12:35:00"
str_mac_target = "08:00:27:08:af:07"

## Check available objects that can be used in scapy.ARP class
# scapy.ls(scapy.ARP)

## 1. Create an ARP Packet
## op=2 is for response (op=1 is for request (Default))
## pdst is the Target IP
## hwdst is the Target MAC
## psrc is the Access Point AP
obj_packet_arp = scapy.ARP(op=2, pdst=str_ip_target, hwdst=str_mac_target, psrc=str_ip_ap)
## Check the packet details
print(obj_packet_arp.show())
print(obj_packet_arp.summary())