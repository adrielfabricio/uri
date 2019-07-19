"""
URI 1098 - Sequencia IJ 4

@author Adriel Fabricio
"""

I = 0
J = 1
marker = 0
while I <= 2:
    if I == 0.0 or I == 1.0 or round(I) == 2.0:
        print('I=%d J=%d' % (I, J + I))
    else:
        print('I=%.1f J=%.1f' % (I, J + I))

    marker += 1
    J += 1
    if marker == 3:
        I += 0.2000
        J = 1
        marker = 0
