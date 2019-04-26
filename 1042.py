'''
URI 1042 - Sort Simples

@author Adriel Fabricio
'''
x, y, z = map(int, input().split())
if x > y and y > z:
    maior = x
    mid = y
    menor = z
if x > y and z > y:
    maior = x
    mid = z
    menor = y
if y > x and x > z:
    maior = y
    mid = x
    menor = z
if y > x and z > x:
    maior = y
    mid = z
    menor = x
if z > x and x > y:
    maior = z
    mid = x
    menor = y
if z > y and y > x:
    maior = z
    mid = y
    menor = x

print(menor)
print(mid)
print(maior)
print('')
print(x)
print(y)
print(z)
