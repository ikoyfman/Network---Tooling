import platform
import os
import ipaddress


def network_scan(address="192.168.1.0", subnet=str(30)):
    #Get all usable hosts
    formated_address = address + "/" + subnet
    hosts = list(ipaddress.IPv4Network(formated_address).hosts())
    
    #Ping all hosts capture response
    results = ping_host(hosts)
    return results

def ping_host(ipaddresses):
    #Figure out Operating system
    oper = platform.system()
    if (oper == "Windows"):
        ping = "ping -n 1"
    elif (oper == "Linux"):
        ping = "ping -c 1"
    else:
        ping = "ping -c 1"
    
    hosts_response = []
    for address in ipaddresses:
        formated_ping = ping + ' ' + str(address)
        print(formated_ping)
        response = os.popen(formated_ping)
        for text in response:
            if text.count('ttl='):
                hosts_response.append("{} is alive".format(address))
                
                
    return hosts_response
    
results = (network_scan('192.168.10.0','28'))
print(results)