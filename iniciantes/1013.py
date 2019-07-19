a, b, c = map(int, input().split())

maiorAB = (a + b + abs(a - b))/2
maiorBC = (b + c + abs(b - c))/2

if maiorAB > maiorBC:
    print("%d eh o maior" % maiorAB)
else:
    print("%d eh o maior" % maiorBC)
