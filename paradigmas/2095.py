"""
URI 2095 - Guerra

@author Adriel Fabricio
"""
S = int(input())

quadr = []
noglo = []

quadr.extend(map(int, input().split()))
noglo.extend(map(int, input().split()))
quadr.sort()
noglo.sort()

win = i = j = 0
while i < len(noglo):

    minQ = quadr[j]
    minN = noglo[i]
    if (minN - minQ) > 0:
        win += 1
        i += 1
        j += 1
    else:
        i += 1


print(win)
