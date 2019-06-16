import sys
import os
from network_scanner_module.port_scanner_threading import scan_ports,tcp_connect

def test_google_open():
    test_ip1 = tcp_connect('google.com',80)
    test_ip2 = tcp_connect('google.com',443)
    test_ip3 = tcp_connect('google.com',53)
    assert test_ip1 == True
    assert test_ip2 == True
    assert test_ip3 == False

def test_port_scan_multiple():
    results = scan_ports('google.com',1,500)
    assert results[443] == True
    assert results[80] == True
    assert results[500] == False