"""
URI 1114 - Senha Fixa

@author Adriel Fabricio
"""
mask = 2002
password = int(input())
if (mask == password):
    print('Acesso Permitido')
else:
    print('Senha Invalida')
    while True:
        password = int(input())
        if (mask == password):
            print('Acesso Permitido')
            break
        else:
            print('Senha Invalida')
