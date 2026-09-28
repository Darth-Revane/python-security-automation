import socket

target = "127.0.0.1"
ports = [80, 443, 8834, 15150]

for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.settimeout(1)
        result = connection.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open on {target}")
    else:
        print(f"Port {port} is closed or unavailable on {target}")