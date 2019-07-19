""""
URI 1080 - Maior e Posição

@author Adriel Fabricio
"""

n = []
for i in range(100):
    n.append(int(input()))

m = n[0]
idx = 0
for i in range(1, len(n)):
    if (n[i] > m):
        m = n[i]
        idx = n.index(n[i])

print(m)
print(idx + 1)
