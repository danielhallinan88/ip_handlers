import ip_handlers

test_val1 = 3402823669209384634633746074317
test_val2 = 42541956123769884636017138956568135816 #Should = 2001:4860:4860::8888
test_val3 = 4294967294 # 255.255.255.254
test_val4 = '10.27.2.0/28'

print(test_val2)
val   = ip_handlers.Integer(test_val2)
val_6 = val.int_to_ipv6()
print(val_6)

val_6_int = ip_handlers.IPv6(val_6).ipv6_to_int()
print(val_6_int)

ips = ip_handlers.all_addr_in_subnet(test_val4)
print(test_val4)
print(ips)
