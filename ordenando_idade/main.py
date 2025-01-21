import glob
import os


files = ["./arquivo1.txt", "./arquivo2.txt", "./arquivo3.txt"]

dados = []


for file in files:
    with open(file, "r") as f:
        for linha in f:
            nome, idade = linha.strip().split(",")
            dados.append((nome, int(idade)))

dados_ordenados = sorted(dados, key=lambda x: x[1])     ### definindo que sera ordenado pela idade

with open("dados_ordenados.txt", "w") as f:
    for nome, idade in dados_ordenados:
        f.write(f"{nome} -> {idade}\n")