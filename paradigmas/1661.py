"""
URI 1661 - Comércio de Vinhos da Gergóvia

@author Adriel Fabricio
"""

while True:
    T = int(input())
    if T == 0:
        break

    a = []
    work = 0
    a.extend(map(int, input().split()))
    for i in range(1, len(a)):
        if (a[i - 1] < 0):
            work += (-1)*a[i - 1]
        else:
            work += a[i - 1]
        a[i] += a[i - 1]
    print(work)
