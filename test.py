import sys
import os
from network_scanner_module.port_scanner import pscan

def test_google_open():
    test_ip1 = pscan('google.com',80)
    test_ip2 = pscan('google.com',443)
    test_ip3 = pscan('google.com',53)
    assert test_ip1 == "Opened!"
    assert test_ip2 == "Opened!"
    assert test_ip3 == "Closed"