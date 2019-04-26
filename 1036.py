import math

a, b, c = map(float, input().split())

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
