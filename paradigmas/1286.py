"""
URI 1286 - Motoboy

@author Adriel Fabricio
"""
NMAX = 21
PMAX = 31


def knap_sack(W, wgt, val):
    K = [[0 for x in range(PMAX)] for x in range(NMAX)]
    i = 0
    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            else:
                if (wgt[i - 1] > w):
                    K[i][w] = K[i-1][w]
                else:
                    K[i][w] = max(K[i-1][w-wgt[i-1]] + val[i-1], K[i - 1][w])
    return K[N][W]


while True:
    tempo_total = []
    qnt_pizza = []
    N = int(input())
    if N == 0:
        exit()
    P = int(input())

    for i in range(N):
        temp_tempo, temp_pizza = map(int, input().split())
        tempo_total.append(temp_tempo)
        qnt_pizza.append(temp_pizza)

    tempo_gasto = knap_sack(P, qnt_pizza, tempo_total)

    print('%d min.' % tempo_gasto)
