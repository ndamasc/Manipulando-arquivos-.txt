import re

file = "./log.txt"
ip = []
ip_rgx = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

with open(file, "r") as f:
    for linha in f:
        match = re.search(ip_rgx, linha)
        if match:
            ip.append(match.group())

print(f"IPs encontrados:\n{ip}")