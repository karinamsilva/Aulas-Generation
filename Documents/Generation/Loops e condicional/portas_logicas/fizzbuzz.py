#Autor: Karina 

#FizzBuzz V1
# Descrição: Exercicio que imprime numeros de 1 a 100, sempre que o número é multiplo de 3 imprime fizz
#Sempre que é multiplo de 5 imprime buzz
#Se for multiplo de 3 e 5 imprime fizzbuzz

numero = 1 

#Aula FizzBuzz usando while 
#Versão do professor

'''while numero <= 100:
    if numero % 3 == 0:
        if numero % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif numero % 5 == 0:
        print('buzz')
    else:
        print(numero)
    numero+=1   '''

#Usando and no loop while

'''while numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print('fizzbuzz')
    elif numero % 3 == 0:
        print('fizz')
    elif numero % 5 == 0:
        print('buzz')
    else:
        print(numero)
    numero+=1'''

#Usando loop for:

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
