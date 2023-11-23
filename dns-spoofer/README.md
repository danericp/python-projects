## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 3
* A target machine (Tested in Parrot OS)
* A network connection (wired or wireless) for the machines
* iptables setup before using the program
```
iptables -I FORWARD -j NFQUEUE --queue-num 0
iptables -I OUTPUT -j NFQUEUE --queue-num 0
iptables -I INPUT -j NFQUEUE --queue-num 0
```

## Module Requirements

* [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse): The argparse module makes it easy to write user-friendly command-line interfaces.
* [NetfilterQueue ](https://pypi.org/project/NetfilterQueue/): NetfilterQueue provides access to packets matched by an iptables rule in Linux. Packets so matched can be accepted, dropped, altered, reordered, or given a mark.
* [scapy](https://scapy.readthedocs.io/en/latest/): Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.

## Output

A continuous output of DNS details. The target DNS browser destination should change according to your payload.
This can be stopped by a keyboard interruption CTRL+C.

* Flush iptables after use.
```
iptables --flush
```

## Process

1. Setup iptables.
2. Send a running Scapy process, wait for the target to browse the internet and send DNS packets
3. Wait for Scapy to catch this specific DNS packet that aligns to your desired DNS to be spoofed (E.g. www.bing.com)
4. Scapy will edit this packet and inject your IP address as a payload.
5. Forward the malicious packet to the target.
6. Flush iptables.

## Usage

```
usage: DNS Spoofer [-h] -d DNS -p PAYLOAD

Sends Payload via Target DNS input. MITM is required

optional arguments:
  -h, --help            show this help message and exit
  -d DNS, --domain-name DNS
                        DNS (E.g. www.bing.com)
  -p PAYLOAD, --payload PAYLOAD
                        IPv4 Rerouting Address (E.g. 192.168.1.5)
```

## References

* [Jason Sohl](https://www.jasonsohl.com/netfilterqueue-on-parrotos/): NetfilterQueue on ParrotOS
* [Stack Overflow](https://stackoverflow.com/questions/61098923/typeerror-argument-payload-has-incorrect-type-expected-bytes-got-str-how): TypeError: Argument 'payload' has incorrect type (expected bytes, got str). How can I fix it? Why it works on Python 2 but not using Python 3?
* [Stack Overflow](https://stackoverflow.com/questions/22130342/scapy-attributeerror-on-every-call-module-object-has-no-attribute): Scapy AttributeError on every call: 'module' object has no attribute '*'