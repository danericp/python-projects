
print("Importing the Python module for enabling network scanning")
import argparse
import scapy.all as scapy

int_line_length=50
str_ip = "192.168.1.4/24"

def do_scan_ip(str_ip):
    ## Example ARP Request without specifying your target IP
    # obj_arp_request = scapy.ARP()
    ## Check what the object is trying to do
    ## ARP who has 0.0.0.0 says 192.168.1.78
    # print(obj_arp_request.summary())
    ## Check the sub classes of the Scapy ARP request object/class
    # scapy.ls(scapy.ARP())

    ## 1. Create an ARP request directed to broadcast MAC asking for IP
    
    ##  1.a. Use ARP to ask who has the target IP
    obj_arp_request = scapy.ARP(pdst=str_ip)
    # arp_request.pdst = str_ip # Option 2
    # print(obj_arp_request.summary())
    ## Display the contents of the ARP request object
    # obj_arp_request.show()
    
    ## 1.b. Set destination MAC to broadcast MAC.
    ## Make sure that the ARP request will be sent to all clients on the same network.
    ## Ethernet frame is required since data in network is sent using MAC Addresses, not IP Addresses.
    ## Destination MAC Address is set to the ethernet part of each packet, not in any other part.
    ## Create an ethernet frame, then append our IP request later.
    # obj_broadcast = scapy.Ether()
    ## Check the sub classes of the Scapy ethernet object/class
    # scapy.ls(scapy.Ether())
    ## Create a Ethernet frame Object/Class to broadcast the ARP request
    ## MAC broadcast address is ff:ff:ff:ff:ff
    obj_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ## Check what the Ethernet frame Object/Class is trying to do
    ## 3e:ba:3e:28:3e:3e > ff:ff:ff:ff:ff:ff (0x9000)
    # print(obj_broadcast.summary())
    ## Create a packet that will contain both ARP request and ethernet broadcast. Append using forward slash
    obj_arp_broadcast = obj_broadcast/obj_arp_request
    ## Check what the obj_arp_broadcast is trying to do
    ## Ether / ARP who has str_ip says 192.168.1.78
    # print(obj_arp_broadcast.summary())
    ## Display the contents of the ethernet broadcast object
    # obj_arp_broadcast.show()
    
    ## 2. Send the packet (containing ARP request and ethernet broadcast) and receive the response
    
    ## scapy.sr() = Send and Receive
    ## scapy.srp(obj_packet) = Send and Receive Packet (Customer header part -> Ether)
    ## Send the packet using srp and capture the response in two variables
    # list_response_answered, list_response_unanswered = scapy.srp(obj_arp_broadcast)
    ## Adding a timeout of 1 second. Highly recommended
    list_response_answered, list_response_unanswered = scapy.srp(obj_arp_broadcast, timeout=1)
    # Check the contents of the answered/unanswered response
    # print(list_response_answered.summary())
    # print(list_response_unanswered.summary())
    ## Capture only the answered list
    # list_response_answered = scapy.srp(obj_arp_broadcast, timeout=1)[0]
    ## Make the response less verbose
    list_response_answered = scapy.srp(obj_arp_broadcast, timeout=1, verbose=False)[0]

    list_clients = []
    for idx_answer in list_response_answered:
        dict_client = {"ip": idx_answer[1].psrc, "mac": idx_answer[1].hwsrc}
        list_clients.append(dict_client)
        ## Printing the whole index
        ## This contains two sub index = query=0, answer=1
        # print(("="*int_line_length) + "\n" + str(idx_answer) + "\n" + ("="*int_line_length))
        ## Print only the answer
        # print(("="*int_line_length) + "\n" + str(idx_answer[1]) + "\n" + ("="*int_line_length))
        ## Print only the answer (detailed)
        # print(("="*int_line_length) + "\n" + str(idx_answer[1].show()) + "\n" + ("="*int_line_length))
        ## Print only the answer IP of the source
        # print(("="*int_line_length) + "\n" + str(idx_answer[1].psrc) + "\n" + str(idx_answer[1].hwsrc) + "\n" + ("="*int_line_length))
        ## Refined printing
        # print(idx_answer[1].psrc + "\t\t" + idx_answer[1].hwsrc)
    return list_clients

def do_print(list_result):
    print("IP" + "\t\t\t" + "MAC Address" + "\n" + ("="*int_line_length))
    for dict_client in list_result:
        print(dict_client["ip"] + "\t\t" + dict_client["mac"])

def get_arguments():
    obj_parser = argparse.ArgumentParser(
        prog='Network Scanner',
        description='Scan neighbor IP addresses',
        epilog='Works with Python 3'
    )
    obj_parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = obj_parser.parse_args()
    return options

obj_options = get_arguments()
list_result = do_scan_ip(obj_options.target)
do_print(list_result)