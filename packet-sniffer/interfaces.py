from scapy.all import ifaces

# Print human-readable information about available interfaces
for interface, details in ifaces.data.items():
    print(f"Interface Name: {interface}")
    print("Details:")
    print(f"\tDescription: {details.description}")
    print(f"\tIP: {details.ip}")
    print(f"\tMAC: {details.mac}")
    print("\n")
