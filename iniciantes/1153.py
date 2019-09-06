"""
URI 1153 - Fatorial Simples

@author Adriel Fabricio
"""


def factorial(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    else:
        x = factorial(n-1) * n
        memo[n] = x
        return x


memo = {}
N = int(input())
print(factorial(N))
