from exercicio import Conta

conta = Conta()

conta.numeros = input("Digite o numero da sua conta: ")
conta.titular = input("Digite o nome do titular da sua conta: ")
conta.saldo = input("Digite o saldo da sua conta: ")
conta.limite = input("Digite o limite da sua conta: ")

print(conta)

