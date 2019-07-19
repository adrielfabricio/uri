'''
URI 1079 - Médias Ponderadas

@author Adriel Fabricio
'''


def media_ponderada(val):
    media = (val[0]*2 + val[1]*3 + val[2]*5) / 10
    return media


N = int(input())
for i in range(N):
    valores = []
    valores.extend(map(float, input().split()))
    media = media_ponderada(valores)
    print('%.1f' % media)
