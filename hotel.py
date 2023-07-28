# Laço de repetição FOR

print("Bem vindo ao HOTEL CONFORTO.")
for numero in range(0, 21, 1):
    numero = numero + 1
    if(numero == 13):
        continue
    if(numero == 21):
        break
    print(numero, "ª andar")

# Laço de repetição WHILE

print("Bem vindo ao HOTEL CONFORTO.")
predio = 0
while(predio < 20):
    predio = predio + 1  
    if(predio == 13):
        continue
    if(predio == 21):
        break
    print(predio, "ª andar")  

 # laço de repetição decrescente FOR   

print("Bem vindo ao HOTEL CONFORTO.")
for andar in range(21 , 1, -1):
    andar = andar - 1
    if(andar == 13):
        continue
    if(andar == 21):
        break
    print(andar, "ª andar")
    
  



