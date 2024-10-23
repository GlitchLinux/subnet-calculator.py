import ipaddress

def calculate_subnets(ip_address, prefix):
    # Create a network object using the provided IP address and prefix
    network = ipaddress.IPv4Network(f"{ip_address}/{prefix}", strict=False)

    # Prepare output for subnets
    subnets = []

    # Calculate the size of each subnet
    subnet_size = 2 ** (32 - network.prefixlen)

    # Calculate the number of subnets based on the prefix
    num_subnets = 2 ** (network.prefixlen - 24) if network.prefixlen > 24 else 1

    # Calculate and store all subnets
    for i in range(num_subnets):
        # Calculate the network address for each subnet
        current_network = ipaddress.IPv4Address(network.network_address + (i * subnet_size))
        first_ip = current_network + 1  # First usable IP
        last_ip = current_network + subnet_size - 2  # Last usable IP
        broadcast_ip = current_network + subnet_size - 1  # Broadcast IP

        subnets.append((current_network, first_ip, last_ip, broadcast_ip))

    return subnets

def display_subnets(ip_address, prefix, subnets):
    print(f"\nSubnetting {ip_address} with a /{prefix} results in:\n")
    print(f"{'ID':<16} {'First / Last':<36} {'Broadcast':<16}")
    print('-' * 80)

    for subnet in subnets:
        network_id, first_ip, last_ip, broadcast_ip = subnet
        # Adjust the spacing for more symmetrical output
        print(f"{str(network_id):<16} | {str(first_ip):<15} - {str(last_ip):<15} | {str(broadcast_ip):<16}")

    # Display the subnet mask based on the provided prefix
    subnet_mask = ipaddress.IPv4Network(f"{ip_address}/{prefix}").netmask
    print(f"\nSubnet Mask: {subnet_mask}\n")

def is_valid_ip(ip):
    """Validate the IP address format and prevent leading zeros."""
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
        if len(octet) > 1 and octet[0] == '0':  # Check for leading zeros
            return False
    return True

def is_valid_prefix(prefix):
    """Validate the prefix input to ensure it is between /8 and /32."""
    if not prefix.startswith('/'):
        return False
    try:
        value = int(prefix.strip('/'))
        return 8 <= value <= 32
    except ValueError:
        return False

def main():
    while True:
        try:
            print(" ")
            print("¤ Subnet Calculator ¤")
            print(" ")
            # Get user input for IP address
            ip_address = input("Enter IPv4 address: ").strip()
            # Get user input for subnet prefix
            prefix = input("Enter prefix: ").strip()

            # Validate IP address
            if not is_valid_ip(ip_address):
                print("Error: Please enter a valid IPv4 address without leading zeros in any octet.")
                continue

            # Validate subnet prefix
            if not is_valid_prefix(prefix):
                print("Error: Please enter a valid subnet prefix in the format /8 to /32.")
                continue

            # Convert prefix to an integer
            prefix_value = int(prefix.strip('/'))

            # Calculate the subnets
            subnets = calculate_subnets(ip_address, prefix_value)

            # Adjust the IP address to the correct network address
            network_address = ipaddress.IPv4Network(f"{subnets[0][0]}/{prefix_value}", strict=False).network_address

            # Display the calculated subnets and subnet mask
            display_subnets(str(network_address), prefix_value, subnets)

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid IPv4 address and prefix.")
        except KeyboardInterrupt:
            print("\nExiting the subnet calculator.")
            break

if __name__ == "__main__":
    main()
