import re

def is_valid_ipv4(ip_address):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, ip_address)
    if match:
        for octet in match.groups():
            if int(octet) < 0 or int(octet) > 255:
                return False
        return True
    return False

ip_address = input("Enter an IPv4 address: ")
if is_valid_ipv4(ip_address):
    print(f"The IPv4 address '{ip_address}' is valid.")
else:
    print(f"The IPv4 address '{ip_address}' is invalid.")