## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 3 (Python 2 commands have been replaced)
* A target machine (Tested in Windows)
* A network connection (wired or wireless) for the machines

## Module Requirements

* [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse): The argparse module makes it easy to write user-friendly command-line interfaces.
* [scapy](https://scapy.readthedocs.io/en/latest/): Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.
* [time](https://docs.python.org/3/library/time.html?highlight=time): Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.

## Output

A continuous output of sending packets count. This can be stopped by a keyboard interruption CTRL+C.

## Process

1. Send a packet to the target, telling that the attacker is the AP.
2. Send a packet to the AP, telling that the attacker is the target.
3. Repeat the packet sending indefinitely.

## Usage

```
usage: ARP Spoofer [-h] -a AP -t TARGET

Execute MITM

options:
  -h, --help            show this help message and exit
  -a AP, --access-point AP
                        Access Point IPv4 Address (E.g. Router)
  -t TARGET, --target TARGET
                        Target IPv4 Address
```

## References

* [Stack Overflow](https://stackoverflow.com/questions/59720769/unknown-pypcap-network-interface-eth0-error-with-python2-scapy-on-windows-10-m): Unknown pypcap network interface 'eth0' error with python2 scapy on windows 10 machine
* [Tutorialspoint](https://www.tutorialspoint.com/python/python_exceptions.htm): Python - Exceptions Handling
* [Tutorialspoint](https://www.tutorialspoint.com/python/python_loops.htm): Python - Loops