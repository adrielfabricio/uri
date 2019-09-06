"""
URI 1131 - Grenais

@author Adriel Fabricio
"""
win_i = win_g = draw = grenais = 0
new_grenal = 1
while new_grenal == 1:
    inter, gremi = map(int, input().split())
    if inter > gremi:
        win_i += 1
    elif inter < gremi:
        win_g += 1
    else:
        draw += 1
    print('Novo grenal (1-sim 2-nao)')
    new_grenal = int(input())
    grenais += 1
print('%d grenais' % grenais)
print('Inter:%d' % win_i)
print('Gremio:%d' % win_g)
print('Empates:%d' % draw)
if win_i > win_g:
    print('Inter venceu mais')
elif win_i < win_g:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
