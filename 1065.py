"""
URI 1065 - Pares entre Cinco Números

@author Adriel Fabricio
"""
numeros = []
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
cont = 0
for numero in numeros:
    if numero % 2 == 0:
        cont += 1
print('%d valores pares' % cont)
