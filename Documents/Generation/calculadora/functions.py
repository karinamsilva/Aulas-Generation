

def soma(num1,num2):
    return num1 + num2 

def subtracao(num1,num2):
    return num1 - num2 

def divisao(num1,num2):
    if num2 == 0:
            return "Erro, não é possível dividir por zero"
    else:
        return num1 / num2 

def multiplicacao(num1,num2):
    return num1 * num2 


def potencia(num1,num2):
    return num1 ** num2 

def raiz(num1,num2):
    if num2 < 0:
        return "Erro ao calcular"
    else:
        return num1 ** (1/num2)
    
    # Versão com função unica, criando o operador como parametro

'''def calculation(num1,num2,operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 == 0:
            return "Erro, não é possível dividir por zero"
        else:
            return num1 / num2 
    elif operation == '5':
        return num1 ** num2
    elif operation == '6':
        return num1 ** (1/num2)'''

