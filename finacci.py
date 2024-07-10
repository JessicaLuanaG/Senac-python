num1 =int(input("Digite um numero:"))
soma = 0
saida = [1,1]
for i in range(2,num1 ):
    saida.append(saida[i-1] + saida[i-2])
print(saida)