salario = float(input())

if salario >= 0.0 and salario <= 400.0:
    percentual = 15
    reajuste   = salario*(percentual/100)
elif salario > 400.0 and salario <= 800.0:
    percentual = 12
    reajuste   = salario*(percentual/100)
elif salario > 800.0 and salario <= 1200.0:
    percentual = 10
    reajuste   = salario*(percentual/100)
elif salario > 1200.0 and salario <= 2000.0:
    percentual = 7
    reajuste   = salario*(percentual/100)
elif salario > 2000.0:
    percentual = 4
    reajuste   = salario*(percentual/100)

salario += reajuste
print('Novo salario: %.2f' % salario)
print('Reajuste ganho: %.2f' % reajuste)
print('Em percentual: %d %%' % percentual)
