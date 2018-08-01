__author__ = 'Daniel Hallinan'
__date__ = '04/21/2016'

import math


"""
Takes an IP and returns its integer value.
    input:
	- String: 192.168.1.0
    return:
	- int: 3234201856
"""
def addr_ip_to_int(address):
        octets = address.split('.')
        tempIP = [ bin(int(octet))[2:].zfill(8) for octet in octets ]
	return int(''.join(tempIP), 2)


"""
Takes an IP Block and returns a two item tuple containing the integer values of the network address and broadcast address.
	input:
	    - String: 192.168.1.0/24
	return:
	    - tuple: (3234201856, 3234202112)
"""
def first_last_ip(address):
        address = address.split('/')
        host_bits = 2**(32 - int(address[1]))
        net_addr = addr_ip_to_int(address[0])
        broadcast_addr = addr_ip_to_int(address[0]) + host_bits
	return net_addr, broadcast_addr


"""
Takes an IP address and an IP subnet and returns true if the IP is within the subnet's bounds.
	input:
	    - String: 192.168.1.24
	    - String: 192.168.1.0/27
	return:
	    - boolean: True
"""
def in_subnet(address, IPBlock):
        address_int = addr_ip_to_int(address)
        first_addr, last_addr = first_last_ip(IPBlock)
        return address_int >= first_addr and address_int < last_addr


#Returns True or False, whether a subnet block is within the range of a larger block.
def subnet_in_supernet(subnet, supernet):    
        sub_first, sub_last = first_last_ip(subnet)
        super_first, super_last = first_last_ip(supernet)
	return sub_first >= super_first and sub_last <= super_last


def addr_int_to_ip(num):
        octets = []
        num2bin = (bin(num)[2:].zfill(32))
        for x in range(4):
            binOctet = (str(num2bin))[(x * 8):((x + 1) * 8)]
            octets.append(str(int(binOctet, 2)))
        ip = '.'.join(octets)
        return ip


#Give the integer value of 2 IPs and it will return a block with subnet mask.
def ints_to_block(intBlock1, intBlock2): 
        netAddr = addr_int_to_ip(intBlock1)
        hostBits = intBlock2 - intBlock1
        mask = int(32 - math.log(hostBits,2))
        return netAddr + '/' + str(mask)


# Takes an IPv4 block and returns a list of every address.
# Example: 10.0.0.0/30 -> ['10.0.0.0', '10.0.0.1', '10.0.0.2', '10.0.0.3']
def all_addr_in_subnet(addr_block):
	net_addr, broadcast_addr = first_last_ip(addr_block)
	return [ addr_int_to_ip(i) for i in range(net_addr, broadcast_addr) ]


# Converts IPv6 address to integer.
def addr_ipv6_to_int(address):
	full_hex = ''
	hextets = address.split(':')
	hex_count = len(address.split(':'))

	for hextet in hextets:
		if hextet == '':
			full_hex += '0000' * (8 - hex_count + 1)
		else:
			if len(hextet) < 4:
				full_hex += ('0' * (4 - len(hextet))) + hextet
			else:
				full_hex += hextet
	return int(full_hex, 16)
