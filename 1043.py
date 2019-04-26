a, b, c = map(float, input().split())

def is_triangle(a, b, c):
    if (a > (b - c) and a < (b + c)) and (b > (a - c) and b < (a + c)) and (c > (a - b) and c < (a + b)):
        return True
    else:
        return False

if is_triangle(a, b, c):
    x = a + b + c
    # perimetro do triangulo
    print('Perimetro = %.1f' % x)
else:
    x = ((a + b)*c)/2
    # area do trapezio
    print('Area = %.1f' % x)
