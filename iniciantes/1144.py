"""
URI 1144 - Sequência Lógica

@author Adriel Fabricio
"""
N = int(input())
seq = cont = 1
jumper = 0

while seq <= N:
    if cont == 1:
        print('%d %d %d' % (seq, seq**2, seq**3))
    elif cont == 2:
        print('%d %d %d' % (seq, seq**2 + 1, seq**3 + 1))
    elif cont == 3:
        seq += 1
        cont = 0
    cont += 1
