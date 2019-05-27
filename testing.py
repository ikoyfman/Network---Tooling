import sys
import os
from network_scanner_module.port_scanner import pscan

# result = Scanner()

for port_number in range(1, 1024):
    result = pscan('atiglobal.com', port_number)

    print("Port {} is {}".format(port_number, result))

# %%
import sys
import os
import platform
import ipaddress
# %%

oper = platform.system()
if (oper == "Windows"):
    ping = "ping -n 1"
elif (oper == "Linux"):
    ping = "ping -c 1"
else:
    ping = "ping -c 1"

adder = ipaddress.IPv4Address("192.168.10.1")

formated_ping = ping + ' ' + str(adder)
print(formated_ping)
response = os.popen(formated_ping)

#%%
for words in response:
    print(words.count('ttl='))
