"""
URI 1101 - Sequência de Números e Soma

@author Adriel Fabricio
"""
while True:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    if M > N:
        M, N = N, M
    even_sum = 0
    for i in range(M, N+1):
        print(i, end=" ")
        even_sum += i
    print("Sum=%d" % even_sum)
