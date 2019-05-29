from ipaddress import IPv4Network
from subprocess import Popen, PIPE

def network_scan(address="192.168.1.0", subnet=str(24)):
    # Get all usable hosts
    formated_address = address + "/" + subnet
    hosts = list(IPv4Network(formated_address).hosts())

    # CMD list for 
    cmd_list = [['ping', '-c', '1', hosts[host].compressed]
                for host in range(0, len(hosts))]

    # Ping all hosts capture response
    results = {}
    procs_list = [Popen(cmd, stdout=PIPE) for cmd in cmd_list]
    for proc in procs_list:
        proc.wait()
        if proc.returncode == 0:
            results.setdefault(proc.args[3], True)
        else:
            results.setdefault(proc.args[3], False)
    
    return results

    
results = (network_scan('192.168.10.0','29'))
print(results)