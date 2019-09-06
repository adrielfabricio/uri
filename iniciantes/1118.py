"""
URI 1118 - Várias Notas com  Validação

@author Adriel Fabricio
"""
sum_nota = 0.0
new_calc = count = 1
while new_calc == 1:
    while sum_nota <= 10.0 and count < 3:
        nota = float(input())
        if nota < 0.0 or nota > 10.0:
            print('nota invalida')
        else:
            sum_nota += nota
            count += 1
    print('media = %.2f' % (sum_nota / 2))
    while True:
        print('novo calculo (1-sim 2-nao)')
        new_calc = int(input())
        if new_calc == 1 or new_calc == 2:
            break
    sum_nota = 0.0
    count = 1
