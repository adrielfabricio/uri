"""
URI 1643 - Converter Quilômetros para Milhas

@author Adriel Fabricio
"""


fib_seq = [1, 2]
for i in range(2, 22):
    fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])

t = int(input())
for i in range(t):
    fib_seq.sort(reverse=True)
    x = int(input())
    mask = x
    fib_bin = []

    for i in range(len(fib_seq)):
        if fib_seq[i] <= x:
            fib_bin.append(1)
            x -= fib_seq[i]
        elif mask > x:
            fib_bin.append(0)
    del fib_bin[-1]
    fib_seq.sort()
    fib_bin.reverse()
    result = 0

    for i in range(len(fib_bin)):
        result += fib_bin[i] * fib_seq[i]
    print(result)
