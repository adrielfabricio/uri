'''
URI 1061 - Positivos e Média

@author Adriel Fabricio
'''
numeros = []
numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))

cont = 0
sum = 0.0
for numero in numeros:
    if numero > 0:
        sum += numero
        cont += 1

print('%d valores positivos' % cont)
print('%.1f' % (sum/cont))
