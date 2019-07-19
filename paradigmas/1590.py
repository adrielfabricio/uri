"""
URI 1590 - Cuarenta e Dois

@author Adriel Fabricio
"""


T = int(input())
for i in range(T):
    k_nums = []
    N, K = map(int, input().split())
    k_nums.extend(map(int, input().split()))

    max_AND = 0
    aux = 0
    bit_list = []
    for i in range(29, -1, -1):
        bit = 1 << i
        quantity = 0

        for j in range(len(k_nums) - 1, -1, -1):
            if bit & k_nums[j]:
                quantity += 1
                bit_list.append(j)

        if quantity >= K:
            aux = k_nums[bit_list[0]]
            for j in range(1, quantity - 1):
                aux &= k_nums[bit_list[j]]
            max_AND = max_AND if max_AND > aux else aux
    k_nums = []
    print(max_AND)
