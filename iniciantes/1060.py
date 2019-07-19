'''
URI 1060 - Números Positivos

@author Adriel Fabricio
'''
positivos = []
positivos.append(float(input()))
positivos.append(float(input()))
positivos.append(float(input()))
positivos.append(float(input()))
positivos.append(float(input()))
positivos.append(float(input()))

pos = 0
for i in range(len(positivos)):
    if positivos[i] > 0:
        pos += 1
print('%d valores positivos' % pos)
