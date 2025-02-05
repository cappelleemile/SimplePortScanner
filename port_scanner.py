import socket

# IP or domain to scan
target = input("Enter an IP or domain name: ")

# List of ports to scan (you can expand)
ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]

print(f"Scan from {target}...")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Prevents the script from crashing
    result = s.connect_ex((target, port))  # Trying to connect
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()