# This script runs on Python 3
import socket
import threading
from multiprocessing import Pool
import time



def TCP_connect(ip, port_number):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(.1)
        scanner.connect((str('google.com'), port_number))
        scanner.close()
        return [port_number,True]
    except:
        return [port_number,False]


def scan_ports(host_ip, port_start=None, port_end=None,):
    results = {}

    if port_start and port_end == None:
        connection_result = TCP_connect(host_ip, port_start)
        results[port_start] =  connection_result

    # Prepare list to capture port ranges for multiple ports
    if port_start != port_end and port_end != None:
        port_ranges = []
        end_number = port_start
        for number in range(port_start, port_end+1):
            if number % 100 == 0:
                port_ranges.append((end_number, number))
                end_number = number + 1

        # Go through port ranges
        for port_range in port_ranges:
            port_results = port_scan_threader(host_ip, port_range)
            
        
        for result in port_results:
            print(result)


    return results

def _multiprocess_port_scan_helper(param):
    host_ip = param[0]
    port_numb = param[1]
    return TCP_connect(host_ip,port_numb)

def port_scan_threader(host_ip, port_range):
    ports = []
    for numb in range(port_range[0],port_range[1]+1):
        host_ip_port = [host_ip,numb]
        ports.append(host_ip_port)
    
    p = Pool()
    result_list = p.map(_multiprocess_port_scan_helper,ports)
    p.close()

    return result_list
    


if __name__ == "__main__":
    assert TCP_connect('google.com',80) == {80:True}
    assert TCP_connect('google.com',53) == {53:False}
    
    scan_ports('google.com',1,100)