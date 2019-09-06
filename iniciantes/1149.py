"""
URI 1149 - Somando Inteiros Consecutivos

@author Adriel Fabricio
"""
X = int(input())
Z = int(input())
sum_var = 0
while X >= Z:
    Z = int(input())
i = X
while True:
    sum_var += 1
    if not X >= Z:
        X += i
        i += 1
    else:
        break
    print(X, ' ', i)
print(sum_var)
