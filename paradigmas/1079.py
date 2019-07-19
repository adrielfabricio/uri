"""
1079 - TRANSPORTE DE PAINÉS SOLARES

@author Adriel Fabricio
"""


def binary_search(peso, n_paineis, caminhoes):
    low = max(peso)
    sup = sum(peso)
    while low < sup:
        mid = low + (sup - low) // 2
        prec = 1
        necs = 0
        for i in range(n_paineis):
            if (necs + peso[i]) <= mid:
                necs += peso[i]
            else:
                prec += 1
                necs = peso[i]
        if prec <= caminhoes:
            sup = mid
        else:
            low = mid + 1
    return low


N = int(input())
for i in range(N):
    peso = []

    n_paineis, caminhoes, frete = map(int, input().split())
    peso.extend(map(int, input().split()))

    peso_max = binary_search(peso, n_paineis, caminhoes)
    print('%d $%d' % (peso_max, (peso_max * caminhoes * frete)))
