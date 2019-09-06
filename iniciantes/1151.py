"""
URI 1151 - Fibonnaci Simples

@author Adriel Fabricio
"""


def fibonnaci(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonnaci(n-1, computed) + fibonnaci(n-2, computed)
    return computed[n]


N = int(input())
for i in range(N):
    if i + 1 == N:
        print(fibonnaci(i))
    else:
        print(fibonnaci(i), end=" ")
