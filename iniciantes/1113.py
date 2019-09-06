"""
URI 1113 - Crescente e Decrescente

@author Adriel Fabricio
"""
while True:
    X, Y = map(int, input().split())
    if X == Y:
        break
    if X > Y:
        print('Decrescente')
    else:
        print('Crescente')
