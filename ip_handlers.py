__author__ = 'Daniel Hallinan'
__date__ = '04/21/2016'

import math


# address example: '192.168.1.0', returns integer value of IP
def addr_ip_to_int(address):
        octets = address.split('.')
        tempIP = [ bin(int(octet))[2:].zfill(8) for octet in octets ]
	return int(''.join(tempIP), 2)


# enter IP with mask, example: 192.168.1.0/24)
def first_last_ip(address):
        netBroad = []
        address = address.split('/')
        hostBits = 2**(32 - int(address[1]))
        netAddr = addr_ip_to_int(address[0])
        broadcastAddr = addr_ip_to_int(address[0]) + hostBits
        netBroad.append(netAddr)
        netBroad.append(broadcastAddr)      #returns 2 item list. The first part is the network address, the second part is the broadcast address.
        return netBroad


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
