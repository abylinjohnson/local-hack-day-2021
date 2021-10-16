import socket

def scan(target, ports):
    print("\n" + "Starting scan for " + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened: " +  str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter the target To scan: ")
port = int(input("[*] Enter how many ports to scan: "))
if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), port)
else: 
    scan(targets, port)
