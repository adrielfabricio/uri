'''
URI 1071 - Soma de Impares Consecutivos I

@author Adriel Fabricio
'''
X = int(input())
Y = int(input())

sum = 0
if X == Y:
    print(sum)
    exit()
if X > Y:
    for i in range(Y+1, X):
        if i % 2 == 1:
            sum += i
if X < Y:
    for i in range(X+1, Y):
        if i % 2 == 1:
            sum += i
print(sum)
