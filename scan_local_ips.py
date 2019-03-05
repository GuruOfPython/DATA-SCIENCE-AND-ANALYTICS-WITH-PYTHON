from socket import *
network = '192.168.1.'
def is_up(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.01)    ## set a timeout of 0.01 sec
    if not s.connect_ex((addr,135)):    # connect to the remote host on port 135
        s.close()                       ## (port 135 is always open on Windows machines, AFAIK)
        return 1
    else:
        s.close()

def run():
    for ip in range(1,256):    ## 'ping' addresses 192.168.1.1 to .1.255
        addr = network + str(ip)
        if is_up(addr):
            print('%s \t- %s' %(addr, getfqdn(addr)))    ## the function 'getfqdn' returns the remote hostname

run()
