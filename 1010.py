cod1, gear1, value1 = input().split()
cod2, gear2, value2 = input().split()

total = (float(gear1)*float(value1) + float(gear2)*float(value2))

print('VALOR A PAGAR: R$ %.2f' % total)
