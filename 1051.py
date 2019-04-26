salario = float(input())

total = 0.0

if salario <= 2000.0:
    print('Isento')
else:
    if salario > 2000.0 and salario <= 3000.0:
        total = (salario - 2000.0)*(0.08)
    if salario > 3000.0 and salario <= 4500.0:
        total = (salario - 3000.00)*(0.18) + (1000.0)*(0.08)
    if salario > 4500.0:
        total = (salario - 4500.0)*(0.28) + (1500.0)*(0.18) + (1000.0)*(0.08) 
    print('R$ %.2f' % total)
