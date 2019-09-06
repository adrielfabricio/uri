"""
URI 1117 - Validação de Nota

@author Adriel Fabricio
"""
sum_nota = 0.0
while sum_nota <= 10.0:
    nota = float(input())
    if nota < 0.0 or nota > 10.0:
        print('nota invalida')
    else:
        sum_nota += nota
print('media = %.2f' % (sum_nota / 2))
