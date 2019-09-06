"""
URI 1134 - Tipo de Combustível

@author Adriel Fabricio
"""
alco = gaso = dies = 0
while True:
    code = int(input())
    if code == 4:
        break
    if code == 1:
        alco += 1
    elif code == 2:
        gaso += 1
    elif code == 3:
        dies += 1
print('MUITO OBRIGADO')
print('Alcool: %d' % alco)
print('Gasolina: %d' % gaso)
print('Diesel: %d' % dies)
