'''
URI 1073 - Quadrado de Pares

@author Adriel Fabricio
'''
N = int(input())

for i in range(1, N+1):
    if i % 2 == 0:
        square = i**2
        print('%d^2 = %d' % (i, square))
