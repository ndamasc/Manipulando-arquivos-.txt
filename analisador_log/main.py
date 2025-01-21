
import os

file = "./logs.txt"

with open(file, "r") as f:
    linhas = f.readlines()

erros = 0

for i, linha in enumerate(linhas, start=1):
    if "ERROR" in linha:
        print(f"Erro na linha {i}:  {linha.strip()}")
        erros +=1

print(f"total de erros: {erros}")