import ip_handlers

test_val1 = 3402823669209384634633746074317
test_val2 = 42541956123769884636017138956568135816 #Should = 2001:4860:4860::8888
test_val3 = 4294967294 # 255.255.255.254
test_val4 = '10.27.2.0/28'
test_val5 = '10.27.2.3'
test_val6 = '10.27.3.33'
test_val7 = '10.27.1.255'
test_val8 = '10.27.2.0/29'
test_val9 = '10.27.2.8/29'
test_val10 = '10.27.2.0/27'
test_val12 = '10.27.2.16/28'

print("{} in {} TEST: {}".format(test_val8, test_val4, ip_handlers.subnet_in_supernet(test_val8, test_val4)))
print("{} in {} TEST: {}".format(test_val9, test_val4, ip_handlers.subnet_in_supernet(test_val9, test_val4)))
print("{} in {} TEST: {}".format(test_val12, test_val4, ip_handlers.subnet_in_supernet(test_val12, test_val4)))

#print("{} in {} TEST: {}".format(test_val5, test_val4, ip_handlers.in_subnet(test_val5, test_val4)))
#print("{} in {} TEST: {}".format(test_val6, test_val4, ip_handlers.in_subnet(test_val6, test_val4)))
#print("{} in {} TEST: {}".format(test_val7, test_val4, ip_handlers.in_subnet(test_val7, test_val4)))
