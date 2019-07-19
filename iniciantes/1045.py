a, b, c = map(float, input().split())

list = [a, b, c]
list.sort(reverse = True)

if list[0] >= list[1] + list[2]:
    print('NAO FORMA TRIANGULO')
else:
    if list[0]**2 == list[1]**2 + list[2]**2:
        print('TRIANGULO RETANGULO')
    if list[0]**2 > list[1]**2 + list[2]**2:
        print('TRIANGULO OBTUSANGULO')
    if list[0]**2 < list[1]**2 + list[2]**2:
        print('TRIANGULO ACUTANGULO')
    if list[0] == list[1] and list[1] == list[2]:
        print('TRIANGULO EQUILATERO')
    elif list[0] == list[1] or list[1] == list[2] or list[0] == list[2]:
        print('TRIANGULO ISOSCELES')
