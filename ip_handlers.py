__author__ = 'Daniel Hallinan'
__date__ = '04/21/2016'

import math
import re
import sys

class IPv4(object):

	def __init__(self):
		pass

	def addr_ip_to_int(self, addr):
		self.addr = addr
	        octets = addr.split('.')
        	temp_ip = [ bin(int(octet))[2:].zfill(8) for octet in octets ]
        	return int(''.join(temp_ip), 2)

	def addr_int_to_ip(self, num):
        	octets = []
        	num_to_bin = (bin(num)[2:].zfill(32))
        	for x in range(4):
                	bin_octet = (str(num_to_bin))[(x * 8):((x + 1) * 8)]
                	octets.append(str(int(bin_octet, 2)))
        	ip = '.'.join(octets)
	        return ip

	def __repr__(self):
		if self.addr:
			return self.addr


class IPv4_Block(IPv4):

	def __init__(self, addr_block):
		self.addr_block = addr_block
		self.net_addr = self.addr_block.split("/")[0]
		self.sub_mask = self.addr_block.split("/")[1]
		
	def first_last_ip(self):
		host_bits = 2**(32 - int(self.sub_mask))
		net_addr_int = IPv4().addr_ip_to_int(self.net_addr)
		broadcast_addr_int = IPv4().addr_ip_to_int(self.net_addr) + host_bits - 1
		return net_addr_int, broadcast_addr_int

	def __repr__(self):
		return self.addr_block


class IPv6(object):

	def __init__(self):
		pass

	def addr_ipv6_to_int(self, addr):
	        full_hex = ''
	        hextets = addr.split(':')
	        hex_count = len(addr.split(':'))
	
	        for hextet in hextets:
	                if hextet == '':
	                        full_hex += '0000' * (8 - hex_count + 1)
	                else:
	                        if len(hextet) < 4:
	                                full_hex += ('0' * (4 - len(hextet))) + hextet
	                        else:
	                                full_hex += hextet
	        return int(full_hex, 16)

	def addr_int_to_ipv6(self, ip_int):
		hex_num = str(hex(ip_int)[2:-1])
		hextets = []
		hex_str = ''
		for num, char in enumerate(hex_num):
			hex_str += char
			if (num + 1) % 4 == 0:
				hextets.append(hex_str)
				hex_str = ''

		#Remove leading zeroes
		for num, hextet in enumerate(hextets):
			if hextet == '0000':
				hextets[num] = '0'
				continue
			tmp_tex = ''
			for char_num, char in enumerate(hextet):
				if char == '0':
					pass
				else:
					tmp_hex = hextet[char_num:]
					hextets[num] = tmp_hex
					break

		zeroes = {'zero_start' : 0, 'zero_stop' : 0, 'zero_count' : 0}
		tmp_zeroes = {'zero_start' : 0, 'zero_stop' : 0, 'zero_count' : 0}
		for num, hextet in enumerate(hextets):
			if hextet == '0':
				tmp_zeroes['zero_start'] = num
				for t_num in range(num, len(hextets)):
					if hextets[t_num] == '0':
						tmp_zeroes['zero_count'] += 1
					else:
						tmp_zeroes['zero_stop'] = t_num
						if tmp_zeroes['zero_count'] > zeroes['zero_count']:
							zeroes = tmp_zeroes
						tmp_zeroes = {'zero_start' : 0, 'zero_stop' : 0, 'zero_count' : 0}
						break
			else:
				pass

		return ':'.join(hextets[:zeroes['zero_start']]) + "::" + ':'.join(hextets[zeroes['zero_stop']:])


def first_last_ip(block):
	net_int, broad_int = IPv4_Block(block).first_last_ip()
	net_ip = IPv4().addr_int_to_ip(net_int)
	broad_ip = IPv4().addr_int_to_ip(broad_int)
	return net_ip, broad_ip

def all_addr_in_subnet(block):
	net_int, broad_int = IPv4_Block(block).first_last_ip()
	return [ IPv4().addr_int_to_ip(i) for i in range(net_int, broad_int + 1) ]

def in_subnet(address, IPBlock):
	addr_int = IPv4().addr_ip_to_int(address)
	net_int, broad_int = IPv4_Block(IPBlock).first_last_ip()
	return addr_int >= net_int and addr_int <= broad_int

def subnet_in_supernet(subnet, supernet):    
	sub_net_int, sub_broad_int = IPv4_Block(subnet).first_last_ip()
	super_net_int, super_broad_int = IPv4_Block(supernet).first_last_ip()
	return sub_net_int >= super_net_int and sub_broad_int <= super_broad_int

h = "2a03:2880:f003:c07:face:b00c::2"
print(h)
i = IPv6().addr_ipv6_to_int(h)
print(i)
j = IPv6().addr_int_to_ipv6(i)
print(j)
