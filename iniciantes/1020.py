n = int(input())

y = int(n / 365)
m = int(n % 365 / 30)
d = int(n % 365 % 30)

print("%d ano(s)" % y)
print("%d mes(es)" % m)
print("%d dia(s)" % d)
