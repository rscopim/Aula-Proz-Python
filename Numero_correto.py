numeroCorreto = False
while(numeroCorreto == False):
    print("Insira um número par")
try:
    numero = int(input())
    if(numero%2==0):
        numeroCorreto = True
        print("Você digitou um número par!")
    else:
        print("Você digitou um número ímpar!")
except:
    print("Caracter inválido, por favor digite um número par")
