import socket  

# IP of domein om te scannen
target = input("Enter an IP or domain name: ")  

# Lijst van poorten om te scannen (je kan uitbreiden)
ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]  

print(f"Scan from {target}...")  

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.settimeout(1)  # Voorkomt dat het script vastloopt  
    result = s.connect_ex((target, port))  # Probeert te verbinden  
    if result == 0:
        print(f"Port {port} is OPEN")  
    s.close()  
