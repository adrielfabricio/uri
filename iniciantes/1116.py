"""
URI 1116 - Dividindo X por Y

@author Adriel Fabricio
"""
N = int(input())

while N:
    X, Y = map(float, input().split())
    div = 0.0
    if Y == 0:
        print('divisao impossivel')
    else:
        div = X / Y
        print('%.1f' % div)
    N -= 1
