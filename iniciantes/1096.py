"""
URI 1096 - Sequencia IJ 2

@author Adriel Fabricio
"""

I = 1
J = 7
while I <= 9:
    print('I=%d J=%d' % (I, J))
    J -= 1
    if (J % 4 == 0):
        J = 7
        I += 2
