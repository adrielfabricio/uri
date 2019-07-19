cod, qnt = map(int, input().split())

if cod == 1:
    total = qnt * 4.00
    print('Total: R$ %.2f' % total)
elif cod == 2:
    total = qnt * 4.50
    print('Total: R$ %.2f' % total)
elif cod == 3:
    total = qnt * 5.00
    print('Total: R$ %.2f' % total)
elif cod == 4:
    total = qnt * 2.00
    print('Total: R$ %.2f' % total)
elif cod == 5:
    total = qnt * 1.50
    print('Total: R$ %.2f' % total)
