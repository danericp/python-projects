## Program Requirements

* Linux-based Operating System (Kali, Parrot or Arch)
* Python 2 or 3

## Module Requirements

* [subprocess](https://docs.python.org/3/library/subprocess.html?highlight=subprocess): The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
* [optparse](https://docs.python.org/3/library/optparse.html?highlight=optparse): optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
* [re](https://docs.python.org/3/library/re.html?highlight=re): This module provides regular expression matching operations similar to those found in Perl.

## Output

A confirmation message where if the MAC address has been successfully changed.

## Process

1. Optionally, list all the network interfaces in your machine.
2. Disable the target network interface. You cannot change its MAC address if the interface is enabled.
3. Modify the Ethernet/MAC.
4. Enable the target network interface back.

## Usage

```
Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Target Network Interface
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC Address
```

## References

* [pythex](https://pythex.org/): Python Regular Expression Editor
