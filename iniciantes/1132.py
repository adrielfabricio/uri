"""
URI 1132 - Múltiplos de 13

@author Adriel Fabricio
"""
X = int(input())
Y = int(input())
sum_not_mul = 0
if X > Y:
    X, Y = Y, X
for i in range(X, Y+1):
    if not i % 13 == 0:
        sum_not_mul += i
print(sum_not_mul)
