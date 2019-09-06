"""
URI 1143 - Quadrado e ao Cubo

@author Adriel Fabricio
"""
N = int(input())
n = cont = 1
while N:
    if cont < 3:
        print(n**cont, end=" ")
    elif cont == 3:
        print(n**cont)
    cont += 1
    if cont == 4:
        n += 1
        N -= 1
        cont = 1
