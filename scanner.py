import socket
import sys
from datetime import datetime

def scan_ports(target):
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    # Scanning common ports (FTP, SSH, HTTP, HTTPS)
    common_ports = [21, 22, 80, 443, 8080]
    
    try:
        for port in common_ports:
            # AF_INET is IPv4, SOCK_STREAM is TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
            
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
        scan_ports(target)
    else:
        print("Invalid amount of arguments.")
        print("Syntax: python scanner.py <ip_or_domain>")