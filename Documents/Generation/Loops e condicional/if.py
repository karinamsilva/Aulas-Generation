#if else
'''idade = int(input('informe sua idade'))

if idade >= 18:
    print('você é maior de idade')
else:
    print('você é maior de idade')'''

#Elif

# a - 9/10 - b 8/7 - c - 6/5 - d - 4/-

nota1 = float(input('informe a nota'))
nota2 = float(input('informe a nota'))
nota3 = float(input('informe a nota'))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    print('A')
elif media >= 7:
    print('B')
elif media >= 5:
    print('C')
else:
    print('D')