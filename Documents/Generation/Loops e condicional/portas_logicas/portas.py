#portas lógicas são divididas em 3 para python
#Porta NOT - negar informação
#Porta OR - porta para condição 
#Porta AND - porta de condição

'''a = True 
b = False 
print("not A:", not a)

print("A or B", a or b)

print("A and B", a and b)'''

idade = 16 
carteira = False 

while idade < 18 or carteira == False:
    pergunta_aniversario = input('você já fez aniversário? ')
    if pergunta_aniversario.lower() == 'sim':
        idade = idade + 1
        print(f"parabens, você tem {idade}")
    pergunta_carta = input('você tirou carta? ')
    if pergunta_carta.lower() == 'sim':
        carteira = True 
    else:
        print('não pode dirigir')
print('pode dirigir')
 

