from controllerfuncoes import salvar 
from controllerfuncoes import relatorio 
from controllerfuncoes import procurarHospedes
from controllerfuncoes import fazerCheckout

def menu():
    
    opcao = 5

    while opcao == 5:

        print(" 1 - Check-In \n 2 - Relatório Hospedes \n 3 - Procurar Hospedes \n 4 - Check-Out \n 5 - Finalizar Atendimento")
        opcao = int(input("Digite sua opcão para proseguir: "))     

        if opcao == 1:
            hotel_cliente = {}
            hotel_cliente["nome"] = input(("Digite seu nome: "))
            hotel_cliente["sobrenome"] = input(("Digite seu sobrenome: "))
            hotel_cliente["idade"] = input(("Digite sua idade: "))
            salvar(hotel_cliente)
                
        elif opcao == 2:  
            print("A lista de nomes inseridos \n", relatorio())  
        
        elif opcao == 3:
            clienteFind = str(input("Digite o nome que queria encontrar: "))
            procurarHospedes(clienteFind)
        elif opcao == 4:
            clienteFind = str(input("Digite o nome que queria fazer check out: "))
            fazerCheckout(clienteFind)
        
    print(" 1 - Check-In \n 2 - Relatório Hospedes \n 3 - Procurar Hospedes \n 4 - Check-Out \n 5 - Finalizar Atendimento")
    opcao = int(input("Digite sua opcão para proseguir: "))          
         

menu()
