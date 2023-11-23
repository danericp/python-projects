## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 3 (Python 2 commands have been replaced)
* A target machine (Tested in Windows)
* A network connection (wired or wireless) for the machines

## Module Requirements

* [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse): The argparse module makes it easy to write user-friendly command-line interfaces.
* [scapy](https://scapy.readthedocs.io/en/latest/): Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.
* [scapy-http](https://github.com/invernizzi/scapy-http): Support for HTTP in Scapy. This has become deprecated and moved as part of native support.

## Output

A continuous output of sending packets count. This can be stopped by a keyboard interruption CTRL+C.

## Process

1. Send a packet to the target, telling that the attacker is the AP.
2. Send a packet to the AP, telling that the attacker is the target.
3. Repeat the packet sending indefinitely.

## Usage

```

```

## References

* [Tutorialspoint](https://www.tutorialspoint.com/python/python_exceptions.htm): Python - Exceptions Handling
* [Tutorialspoint](https://www.tutorialspoint.com/python/python_loops.htm): Python - Loops
