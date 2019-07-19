""""
URI 1094 - Experiências

@author Adriel Fabricio
"""

N = int(input())

soma = q_rato = q_sapo = q_coelho = 0
for i in range(N):
    quantia, tipo = map(str, input().split())
    soma += int(quantia)
    if tipo == 'R':
        q_rato += int(quantia)
    elif tipo == 'S':
        q_sapo += int(quantia)
    elif tipo == 'C':
        q_coelho += int(quantia)


print('Total: %d cobaias' % soma)
print('Total de coelhos: %d' % q_coelho)
print('Total de ratos: %d' % q_rato)
print('Total de sapos: %d' % q_sapo)
print('Percentual de coelhos: %.2f %%' % ((q_coelho / soma) * 100))
print('Percentual de ratos: %.2f %%' % ((q_rato / soma) * 100))
print('Percentual de sapos: %.2f %%' % ((q_sapo / soma) * 100))
