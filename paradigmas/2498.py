"""
2498 - AJUDE VÂNIA

@author Adriel Fabricio
"""


def knap_sack(W, pesos, poder_l, N):
    K = [[0 for x in range(W + 1)] for x in range(N + 1)]

    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            else:
                if (pesos[i-1] > w):
                    K[i][w] = K[i-1][w]
                else:
                    K[i][w] = max(K[i-1][w - pesos[i-1]] +
                                  poder_l[i-1], K[i - 1][w])
    return K[N][W]


n = 1
while n:
    list_peso = []
    list_grau = []
    n_livros, capacidade_bolsa = map(int, input().split())

    if not n_livros and not capacidade_bolsa:
        exit()

    for i in range(n_livros):
        peso_livro, grau_interesse = map(int, input().split())
        list_peso.append(peso_livro)
        list_grau.append(grau_interesse)

    print('Caso %d: %d' %
          (n, knap_sack(capacidade_bolsa, list_peso, list_grau, n_livros)))
    n += 1
