"""
URI 1142 - PUM

@author Adriel Fabricio
"""
N = int(input())
cont = 1
while N:
    if not cont % 4 == 0:
        print(cont, end=" ")
    else:
        print('PUM')
        N -= 1
    cont += 1
