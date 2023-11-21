## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 2 or 3

## Module Requirements

* [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse): The argparse module makes it easy to write user-friendly command-line interfaces.
* [scapy](https://scapy.readthedocs.io/en/latest/): Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.

## Output

A tabular output, containing a list of IP address and their correspnding MAC Addresses.

## Process

1. Create an ARP Request packet, asking who has the target IP.
2. Create an Ethernet broadcast packet, where the broadcast MAC address is configured.
3. Combine the two packets and send.
4. Capture all the responses.
5. Parse their contents and print the result.

## Usage

```
usage: Network Scanner [-h] [-t TARGET]

Scan neighbor IP addresses

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP / IP range.
```

## References

* [String literals](https://docs.python.org/2.0/ref/strings.html): Python Escape Characters
