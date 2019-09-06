"""
URI 1133 - Resto da Dvisão

@author Adriel Fabricio
"""
X = int(input())
Y = int(input())
if X > Y:
    X, Y = Y, X
for i in range(X+1, Y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
