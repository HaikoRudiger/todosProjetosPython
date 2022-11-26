from funcao import soma, subtracao, multiplicacao, divisao

def menu():
   print("*"*25, "Menu","*"*25)

   cond = "sim"

   while cond == 'sim':
       n1 = float(input('Digite primeiro numero: '))
       n2 = float(input('Digite segundo numero: '))
       
       print(" 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão")
       opcao = int(input("Digite qual opção você quer efetuar: "))
       
       match opcao:
         case 1:
            print("O resultado é: {:.1f} ".format(soma(n1, n2)))
         case 2:
            print("O resultado é: {:.1f} ".format(subtracao(n1, n2)))
         case 3:
            print("O resultado é: {:.1f} ".format(multiplicacao(n1, n2)))
         case 4:
            print("O resultado é: {:.1f} ".format(divisao(n1, n2)))  
         case _:
            print("Opção invalida")      
       cond = str(input('Deseja continuar? \nsim\nnão\n:>'))

menu()

print('Você saiu da sua aplicação! ')