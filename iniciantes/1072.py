'''
URI 1072 - Intervalo 2

@author Adriel Fabricio
'''
N = int(input())

in_r = out_r = 0
for i in range(N):
    X = int(input())
    if X >= 10 and X <= 20:
        in_r += 1
    else:
        out_r += 1
print('%d in' % in_r)
print('%d out' % out_r)
