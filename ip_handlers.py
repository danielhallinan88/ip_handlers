import math
import re
import sys

__author__ = 'Daniel Hallinan'
__date__   = '04/21/2016'

class Integer(object):
    def __init__(self, num):
        self.num = int(num)

    def int_to_ipv4(self):

        if self.num < 0 or self.num > 4294967294:
            raise ValueError('{} is outside the IPv6 range.'.format(self.num))

        octets     = []
        num_to_bin = (bin(self.num)[2:].zfill(32))

        for x in range(4):
            bin_octet = (str(num_to_bin))[(x * 8):((x + 1) * 8)]
            octets.append(str(int(bin_octet, 2)))

        return '.'.join(octets)

    def int_to_ipv6(self):

        if self.num < 0 or self.num > 340282366920938463463374607431768211455L:
            raise ValueError('{} is outside the IPv6 range.'.format(self.num))

        hex_num = str(hex(self.num)[2:-1])
        hextets = []
        hex_str = ''
        for num, char in enumerate(hex_num):
            hex_str += char
            if (num + 1) % 4 == 0:
                hextets.append(hex_str)
                hex_str = ''

        for num, hextet in enumerate(hextets):
            if hextet == '0000':
                hextets[num] = '0'
                continue
            tmp_tex = ''
            for char_num, char in enumerate(hextet):
                if char == '0':
                    pass
                else:
                    tmp_hex      = hextet[char_num:]
                    hextets[num] = tmp_hex
                    break

        zeroes     = {'zero_start' : 0, 'zero_stop' : 0, 'zero_count' : 0}
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


class IPv4(object):

    def __init__(self, ipv4):
	self.ipv4 = ipv4

    def ipv4_to_int(self):
	octets    = self.ipv4.split('.')
        temp_ip   = [ bin(int(octet))[2:].zfill(8) for octet in octets ]

        return int(''.join(temp_ip), 2)

    def __repr__(self):
	return self.ipv4

class IPv4_Block(IPv4, Integer):

    def __init__(self, ipv4_block):
	self.ipv4_block = ipv4_block
	self.net_addr, self.sub_mask = self.ipv4_block.split("/")
		
    def first_last_ip(self):
	host_bits          = 2**(32 - int(self.sub_mask))
        net_addr_int       = IPv4(self.net_addr).ipv4_to_int()
        broadcast_addr_int = net_addr_int + host_bits - 1
        return Integer(net_addr_int).int_to_ipv4(), Integer(broadcast_addr_int).int_to_ipv4()
#	net_addr_int       = IPv4().addr_ip_to_int(self.net_addr)
#	broadcast_addr_int = IPv4().addr_ip_to_int(self.net_addr) + host_bits - 1
#	return net_addr_int, broadcast_addr_int

    def __repr__(self):
	return self.ipv4_block


class IPv6(object):

    def __init__(self, ipv6):
	self.ipv6 = ipv6

    def ipv6_to_int(self):
	full_hex  = ''
	hextets   = self.ipv6.split(':')
	hex_count = len(hextets)
	
	for hextet in hextets:
	    if hextet == '':
	        full_hex += '0000' * (8 - hex_count + 1)
	    else:
	        if len(hextet) < 4:
	            full_hex += ('0' * (4 - len(hextet))) + hextet
	        else:
	            full_hex += hextet

        return int(full_hex, 16)

def first_last_ipv4(block):
    return IPv4(block).first_last_ip()
#    net_int, broad_int = IPv4_Block(block).first_last_ip()
#    net_ip             = IPv4().addr_int_to_ip(net_int)
#    broad_ip           = IPv4().addr_int_to_ip(broad_int)
#    return net_ip, broad_ip

def all_addr_in_subnet(block):
    net_addr, broad_addr = IPv4_Block(block).first_last_ip()
    net_int   = IPv4(net_addr).ipv4_to_int()
    broad_int = IPv4(broad_addr).ipv4_to_int()
    return [ Integer(i).int_to_ipv4() for i in range(net_int, broad_int + 1) ]
#    net_int, broad_int = IPv4_Block(block).first_last_ip()
#    return [ IPv4().addr_int_to_ip(i) for i in range(net_int, broad_int + 1) ]

def in_subnet(address, IPBlock):
    addr_int           = IPv4().addr_ip_to_int(address)
    net_int, broad_int = IPv4_Block(IPBlock).first_last_ip()
    return addr_int >= net_int and addr_int <= broad_int

def subnet_in_supernet(subnet, supernet):    
    sub_net_int, sub_broad_int     = IPv4_Block(subnet).first_last_ip()
    super_net_int, super_broad_int = IPv4_Block(supernet).first_last_ip()
    return sub_net_int >= super_net_int and sub_broad_int <= super_broad_int
