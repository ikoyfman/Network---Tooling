import socket

def pscan(ip_name, port, type="SOCK_STREAM"):
        # TCP PORT SCAN
        
    if type == "SOCK_STREAM":

        try:
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scanner.settimeout(.1)
            scanner.connect((str(ip_name), port))
            scanner.close()
            return "Opened!"
        except:
            return "Closed"

    """NOT CURRENTLY WORKING
    # UDP PORT SCAN
    if type != "SOCK_STREAM":

        try:
            scanner = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            scanner.bind('127.0.0.1',53)
            scanner.settimeout(2)
            
            return "Opened"
        except:
            return "Closed"
    """          