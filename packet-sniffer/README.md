## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 3 (Python 2 commands have been replaced)
* A target machine (Tested both in Windows and Parrot)
* A network connection (wired or wireless) for the machines
* An HTTP Website. HTTPS is not supported.

## Module Requirements

* [scapy](https://scapy.readthedocs.io/en/latest/): Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.

## Output

A continuous output of HTTP raw contents. This can be stopped by a keyboard interruption.

## Process

1. From your network interface, it will start scanning real-time packets.
2. Process each packet with your desired protocols, port or extensions.
3. Searches for login details and HTTP requests and print them out.

## Usage

This only requires a custom variable input, which is your network interface (E.g. eth0).

## References

* [VulnWeb HTML5](http://testhtml5.vulnweb.com/): Vulnerable HTML5 test website for Acunetix Web Vulnerability Scanner.
* [VulnWeb PHP](http://testphp.vulnweb.com/): TEST and Demonstration site for Acunetix Web Vulnerability Scanner
