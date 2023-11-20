
print("Importing the Python module for enabling subprocesses")
import subprocess
print("Importing the Python module for enabling command arguments")
import optparse
print("Importing the Python module for enabling Regex")
import re

def do_interface_down(str_interface):
    print("Disable the target network interface (" + str_interface + ")")
    # Convert command as an iterable to avoid command injections
    # subprocess.call("ifconfig " + str_interface + " down", shell=True)
    subprocess.call(["ifconfig", str_interface, "down"])
    return 0

def do_change_mac(str_interface, str_new_mac):
    print("Change the MAC Address of the target interface (" + str_interface + ") to " + str_new_mac)
    # Convert command as an iterable to avoid command injections
    # subprocess.call("ifconfig " + str_interface + " hw ether 00:11:22:33:44:55", shell=True)
    subprocess.call(["ifconfig", str_interface, "hw", "ether", str_new_mac])
    return 0

def do_interface_up(str_interface):
    print("Enable back the target network interface")
    # Convert command as an iterable to avoid command injections
    # subprocess.call("ifconfig " + str_interface + " up", shell=True)
    subprocess.call(["ifconfig", str_interface, "up"])
    return 0

def get_arguments():
    print("Create a parser object")
    obj_parser = optparse.OptionParser()
    print("Setup the arguments")
    obj_parser.add_option("-i", "--interface", dest="interface", help="Target Network Interface")
    obj_parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = obj_parser.parse_args()
    if not options.interface:
        obj_parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        obj_parser.error("[-] Please specify a MAC Address, use --help for more info.")
    return options

def get_current_mac(str_interface):
    str_result_ifconfig = subprocess.check_output(["ifconfig", str_interface])
    str_result_ifconfig_new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(str_result_ifconfig))

    if str_result_ifconfig_new_mac:
        return str_result_ifconfig_new_mac.group(0)
    else:
        print("[-] Could not read MAC Address")

obj_options = get_arguments()
do_interface_down(obj_options.interface)
do_change_mac(obj_options.interface, obj_options.new_mac)
do_interface_up(obj_options.interface)
str_current_mac = get_current_mac(obj_options.interface)

if str_current_mac == obj_options.new_mac:
    print("MAC Address has been successfully changed to" + str_current_mac)
else:
    print("MAC Address did not get changed.")