"""
URI 1099 - Soma de Ímpares Consecutives II

@author Adriel Fabricio
"""
N = int(input())

while N:
    X, Y = map(int, input().split())
    if X > Y:
        X, Y = Y, X
    odd_sum = 0
    for i in range(X+1, Y):
        if i % 2 == 1:
            odd_sum += i
    print(odd_sum)
    N -= 1
