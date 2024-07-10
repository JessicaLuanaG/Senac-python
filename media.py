contador = int(0) 
soma = int(0)
add = True
num = 0
while(1):
    pergunt = input("Quer adicionar um numero? ")
    if pergunt=='nao':
        break
    else:
        num = int(input("Escreva um numero "))
        contador += 1
        soma += num
media = soma/contador     
print(media)
        
    