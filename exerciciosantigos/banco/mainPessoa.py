from controller import salvar, listar

def menu():
    print('*'*20, "Menu", '*'*20)

    cond = "sim"
    while cond == "sim":
        salvar(input("Digite seu nome: ")) 
        cond = str(input("Deseja Continuar \n Sim \n Nao \n :> "))

       
menu()

print("A lista de nomes inseridos \n", listar())
