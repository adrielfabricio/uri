"""
URI 1146 - Sequências Crescentes

@author Adriel Fabricio
"""
while True:
    X = int(input())
    if X == 0:
        break
    for k in range(X):
        if k+1 == X:
            print(k+1, end='')
        else:
            print(k+1, end=' ')
    print('')
