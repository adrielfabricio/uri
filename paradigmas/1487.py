"""
URI 1487 - Six Flags

@author Adriel Fabricio
"""


def take_div(brinquedo):
    return brinquedo.div


class Brinquedo:
    def __init__(self, D, P):
        self.D = D
        self.P = P
        self.div = P // D


H = 1

while True:
    brinquedos = []

    N, T = map(int, input().split())

    if N == 0:
        exit()
    for i in range(0, N):
        D, P = map(int, input().split())
        brinquedos.append(Brinquedo(D, P))

    brinquedos.sort(key=take_div, reverse=True)

    total_pontos = 0
    total_tempo = 0

    cont = 0
    while cont < N:
        temp_total_tempo = total_tempo + brinquedos[cont].D
        if temp_total_tempo <= T:
            total_pontos += brinquedos[cont].P
            total_tempo = temp_total_tempo
        else:
            cont += 1

    print('Instancia %d' % H)
    H += 1
    print("%d\n" % total_pontos)
