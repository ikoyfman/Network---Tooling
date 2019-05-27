import platform
import os
import ipaddress


def network_scan(address="192.168.1.0", subnet=str(30)):
    #Get all usable hosts
    formated_address = address + "/" + subnet
    hosts = list(ipaddress.IPv4Network(formated_address).hosts())
    results = {}
    #Ping all hosts capture response
    for host in hosts:
        ping_result = ping_host(host)
        if ping_result == True:
            results.setdefault(host.compressed,True)
        else:
            results.setdefault(host.compressed,False)

    return results

def ping_host(ip_address):
    #Figure out Operating system
    oper = platform.system()
    if (oper == "Windows"):
        ping = "ping -n 1"
    elif (oper == "Linux"):
        ping = "ping -c 1"
    else:
        ping = "ping -c 1"

    formated_ping = ping + ' ' + str(ip_address)
    print(formated_ping)
    response = os.popen(formated_ping)
    for text in response:
        if text.count('ttl='):
            return True
    return False
    
results = (network_scan('192.168.10.0','28'))
print(results)