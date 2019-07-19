"""
1288 - CANHÃO DE DESTRUIÇÃO

@author Adriel Fabricio
"""


def knap_sack(W, pesos, poder_l, C):
    K = [[0 for x in range(W + 1)] for x in range(C + 1)]
    for i in range(C + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            else:
                if (pesos[i-1] > w):
                    K[i][w] = K[i-1][w]
                else:
                    K[i][w] = max(K[i-1][w - pesos[i-1]] +
                                  poder_l[i-1], K[i - 1][w])
    return K[C][W]


C = int(input())
while C:
    poder_l = []
    pesos = []
    projeteis = int(input())

    for i in range(projeteis):
        poder, peso = map(int, input().split())
        poder_l.append(poder)
        pesos.append(peso)

    capacidade_carga = int(input())
    hp_castelo = int(input())

    if knap_sack(capacidade_carga, pesos, poder_l, projeteis) >= hp_castelo:
        print('Missao completada com sucesso')
    else:
        print('Falha na missao')

    C -= 1
