"""
URI 1067 - Seis Números Ímpares

@author Adriel Fabricio
"""
X = int(input())

i = 0
while i < 6:
    if X % 2 == 1:
        print(X)
        i += 1
    X += 1
