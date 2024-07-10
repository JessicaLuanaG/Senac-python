import math
num1 =int(input("Digite um numero:"))
mult = math.floor(num1/2)
if num1 < 2:
    print("Não é primo") 
    exit()
for i in range(2,mult + 1, 1):
    if(not(num1%i)):
        print("Não é primo")
        exit()
        
print("É primo")