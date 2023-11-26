## Important Notes

* Accept-Encoding
* Content-Length

## Module Requirements

* [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse): The argparse module makes it easy to write user-friendly command-line interfaces.
* [NetfilterQueue ](https://pypi.org/project/NetfilterQueue/): NetfilterQueue provides access to packets matched by an iptables rule in Linux. Packets so matched can be accepted, dropped, altered, reordered, or given a mark.
* [Regex](https://docs.python.org/3/library/re.html?highlight=re): This module provides regular expression matching operations similar to those found in Perl.
* [scapy](https://scapy.readthedocs.io/en/latest/): Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.

## Output

A continuous output of HTTP requests and responses. The target HTTP File should change according to your payload.
This can be stopped by a keyboard interruption CTRL+C.

* Stop the ARP Spoofer after use.
* Flush iptables after use.
```
iptables --flush
```

## Process

1. Setup the webserver of your payload E.g. ```service apache2 start```
2. Setup iptables.
```
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT
iptables -I FORWARD -j NFQUEUE --queue-num 0
```
3. Start the ARP Spoofer
4. Enable Packet Forwarding of the MITM E.g. ```echo 1 > /proc/sys/net/ipv4/ip_forward```
5. Start the File Interceptor.
5. From the target, open browser and access an HTTP website. E.g. [SpeedBit](http://www.speedbit.com/)
6. Download a file. The file should be replaced with your payload.

## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 3
* A target machine (Tested in Windows Server)
* A network connection (wired or wireless) for the machines
* iptables setup before using the program

## Usage

```
usage: Code Injector [-h] -p PAYLOAD

Intercepts HTTP Responses via MITM.

options:
  -h, --help            show this help message and exit
  -p PAYLOAD, --payload-alert PAYLOAD
                        Javascript Alert Message
```

## References

* [ChatGPT](https://chat.openai.com/): an AI designed to understand, learn, and help with various tasks and inquiries.
* [Jason Sohl](https://www.jasonsohl.com/netfilterqueue-on-parrotos/): NetfilterQueue on ParrotOS
* [Stack Overflow](https://stackoverflow.com/questions/61098923/typeerror-argument-payload-has-incorrect-type-expected-bytes-got-str-how): TypeError: Argument 'payload' has incorrect type (expected bytes, got str). How can I fix it? Why it works on Python 2 but not using Python 3?
* [Stack Overflow](https://stackoverflow.com/questions/22130342/scapy-attributeerror-on-every-call-module-object-has-no-attribute): Scapy AttributeError on every call: 'module' object has no attribute '*'