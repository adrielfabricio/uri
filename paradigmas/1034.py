"""
1034 - FESTIVAL DE ESTÁTUAS DE GELO

@author Adriel Fabricio
"""
T = int(input())

for k in range(T):
    a = []
    N, M = map(int, input().split())
    a.extend(map(int, input().split()))
    m = [0] * (M+1)
    for i in range(1, M+1):
        m[i] = 1000000
        for j in range(N):
            if (i - a[j] >= 0):
                m[i] = min(m[i], m[i-a[j]] + 1)
    print(m[M])

