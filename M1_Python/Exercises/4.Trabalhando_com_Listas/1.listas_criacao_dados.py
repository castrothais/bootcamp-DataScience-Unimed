frutas = ["laranja", "maca", "uva"]
print(frutas)

lista_vazia = []
print(lista_vazia)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# ACESSO DIRETO

print(frutas[0])
# output: laranja

print(frutas[2])
# output: uva


# INDEXAÇÃO NEGATIVA

print(frutas[-1])
# output: uva

print(frutas[-2])
# output: maca


# MATRIZ

matriz = [[1, "a", 2], ["b", 3, 4], [6, 5, "c"]]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"


# FATIAMENTO
"""Fatiamento significa extrair apenas uma parte (subconjunto) da Lista,
String ou Tupla"""

lista_python = ["p", "y", "t", "h", "o", "n"]

print(lista_python[2:])  # ["t", "h", "o", "n"]
print(lista_python[:2])  # ["p", "y"]
print(lista_python[1:3])  # ["y", "t"]
print(lista_python[0:3:2])  # ["p", "t"]
print(lista_python[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista_python[::-1])  # ["n", "o", "h", "t", "y", "p"]

# ITERAR LISTAS

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# função enumerate: index de carros
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# FILTRAR LISTAS
"""Versão 1"""
lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 200, 400, 700, 1579]
lista_pares = []

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)

"""Versão 2"""
numeros = [1, 30, 21, 2, 9, 65, 34]
"""Retorno, iterável,condição"""
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros_lista = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros_lista]
print(quadrado)
