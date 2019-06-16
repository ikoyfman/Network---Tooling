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

    # UDP PORT SCAN