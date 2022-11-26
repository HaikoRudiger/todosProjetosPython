from conta import Conta
from controller import create, read, update, delete

def menu():

    dados = Conta()

    dados.titular = input("Digite o titular: ")

    dados.numero = input("Digite o numero da conta: ")

    dados.saldo = input("Digite o saldo: ")

    create(dados)

    lista_contas = read()

    print(lista_contas)

    print("*"*30)

    for c in lista_contas:
        print(c)
    
    update_conta = Conta()
        

    update_conta.titular = input("Digite o titular: ")

    update_conta.numero = int(input("Digite o numero da conta: "))

    update_conta.saldo = input("Digite o saldo: ")

    update(update_conta)
    
    lista_contas = read()
    
    for c in lista_contas:
        print(c)
        
    
    delete(int(input("Digite o numero da conta: ")))
    
    lista_contas = read()
    
    for c in lista_contas:
        print(c)

menu()