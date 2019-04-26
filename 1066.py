"""
URI 1066 - Pares, Ímpares, Positivos e Negativos

@author Adriel Fabricio
"""
par = impar = positivo = negativo = 0


def propriedade(numero):
    if numero % 2 == 0:
        global par
        par += 1
    else:
        global impar
        impar += 1
    if numero > 0:
        global positivo
        positivo += 1
    elif numero < 0:
        global negativo
        negativo += 1


numero = int(input())
propriedade(numero)
numero = int(input())
propriedade(numero)
numero = int(input())
propriedade(numero)
numero = int(input())
propriedade(numero)
numero = int(input())
propriedade(numero)

print('%d valor(es) par(es)' % par)
print('%d valor(es) impar(es)' % impar)
print('%d valor(es) positivo(s)' % positivo)
print('%d valor(es) negativo(s)' % negativo)
