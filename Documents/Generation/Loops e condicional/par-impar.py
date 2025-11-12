numero = int(input('insira um numero: '))
segundo_numero = int(input('insira outro numero: '))
soma = numero + segundo_numero
if soma % 2 == 0:
    print(f'{soma} é par')
else:
    print(f'{soma} é impar')