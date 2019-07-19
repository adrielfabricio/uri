"""
URI 1097 - Sequencia IJ 3

@author Adriel Fabricio
"""

I = 1
J = 3
marker = 4
while I <= 9:
    print('I=%d J=%d' % (I, (J + marker)))
    marker -= 1
    if marker == 1:
        marker = 4
        I += 2
        J += 2
