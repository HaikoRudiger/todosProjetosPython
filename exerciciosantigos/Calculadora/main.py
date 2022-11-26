from controller import *

print ("\n Olá, digite a opção desejada e digite os numeros para realizar a operação: \n")

print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLIÇÃO")
print("4 - DIVISÃO")

o = int(input("Digite a opção: "))

n1 = int(input("Por favor, digite o primeiro número: "))
n2 = int(input("Por favor, digite o segundo número: "))
 
if o == 1: 
    print(f"O resultado foi, {soma1(n1,n2)}")

elif o == 2:    
     print(f"O resultado foi, {subtracao(n1,n2)}")

elif o == 3:    
     print(f"O resultado foi, {multiplicacao(n1,n2)}")

elif o == 4:    
     print(f"O resultado foi, {divisao(n1,n2)}")
