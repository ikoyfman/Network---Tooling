from network_scanner_module.port_scanner import pscan

#result = Scanner()

for port_number in range(1,1024):
    result = pscan('atiglobal.com',port_number)
    
    print("Port {} is {}".format(port_number,result))
