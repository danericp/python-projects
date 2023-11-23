#!/usr/bin/env python

import netfilterqueue

def do_packet_process(packet):
    print(packet)
    ## Let the Python program allow/block the packets to the target (Only 1 is allowed)
    packet.accept()
    # packet.drop()

## Create an iptables Queue
# Terminal: iptables -I FORWARD -j NFQUEUE --queue-num 0 

obj_queue = netfilterqueue.NetfilterQueue()
## Bind this object/class to the Terminal iptables Queue
obj_queue.bind(0, do_packet_process)
obj_queue.run()