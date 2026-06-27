import socket
import sys
import time

print("=" * 50)
print("     AUTOMATIC NETWORK PORT SCANNER     ")
print("=" * 50)
print("[+] Looking your local network...")


try:
    
    s_detect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_detect.connect(("8.8.8.8", 80))
    my_ip = s_detect.getsockname()[0]
    s_detect.close()
    
    
    ip_parts = my_ip.split('.')
    target = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.1"
    
except Exception:
    
    target = "192.168.1.15"

print(f"[+] IP Target detected automatically: {target}")
print("[+] Starting to scan port 1 - 1024...")
print("-" * 50)
time.sleep(0.5)


try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1) 
        
        result = s.connect_ex((target, port))
        
        
        if result == 0:
            print(f"-> Port {port}:  (Open) [!] ")
        
        s.close()

except KeyboardInterrupt:
    print("\n[-] Stopped.")
    sys.exit()

print("-" * 50)
print("[+] Scanning done.")
print("=" * 50)

