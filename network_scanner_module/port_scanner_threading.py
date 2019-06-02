# This script runs on Python 3
import socket
import threading
from multiprocessing import Pool



def TCP_connect(port_number, ip='google.com', delay='.5'):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        scanner.connect((str('google.com'), port_number))
        scanner.close()
        return True
    except:
        return False


def scan_ports(host_ip, port_start=None, port_end=None,):
    results = []

    if port_start and port_end == None:
        connection_result = TCP_connect(host_ip, port_start)
        results.append(
            {port_start: connection_result}
        )

    # Prepare list to capture port ranges for multiple ports
    if port_start != port_end and port_end != None:
        port_ranges = []
        end_number = port_start
        for number in range(port_start, port_end+1):
            if number % 20 == 0:
                port_ranges.append((end_number, number))
                end_number = number + 1

        # Go through port ranges
        for port_range in port_ranges:
            port_scan_threader(host_ip, port_range)
            #results.append(port_range_results)

    return results

def _multiprocess_map_helper(param):
    host_ip = param[0]
    port_numb = param[1]
    return TCP_connect(port_numb,host_ip)

def port_scan_threader(host_ip, port_range):
    ports = []
    for numb in range(port_range[0],port_range[1]+1):
        host_ip_port = [host_ip,numb]
        ports.append(host_ip_port)
    print(ports)
    p = Pool()
    result_list = p.map(_multiprocess_map_helper,ports)
    print(result_list)


if __name__ == "__main__":
    #assert TCP_connect('google.com',80) == True
    #assert TCP_connect('google.com',53) == False

    print(scan_ports('google.com', 1,100))
 