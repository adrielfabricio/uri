n1, n2, n3, n4 = map(float, input().split())

media = (n1*2 + n2*3 + n3*4 + n4)/10

print('Media: %.1f' % media)

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 7.0:
    print('Aluno em exame.')
    nf = float(input())
    print('Nota do exame: %.1f' % nf)
    mediaf = (media + nf)/2
    if media >= 5.0:
        print('Aluno aprovado.')
    elif media <= 4.9:
        print('Aluno reprovado.')
    print('Media final: %.1f' % mediaf)
