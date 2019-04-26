a, b = map(int, input().split())

def is_multiple(a, b):
    maior = max(a, b)
    menor = min(a, b)
    if maior % menor == 0:
        return True
    else:
        return False

if is_multiple(a, b):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
