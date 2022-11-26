


from time import sleep

cadastro = 0

dados = []

while cadastro != 3:

 
    print("Você quer Cadastrar os seus dados ou você seguir de forma anonima?\n")
    print("1 - Opção Cadastrar")
    print("2 - Opção Anonima")
    print("3 - Exibir todos os Cadastro")
    print("4 - SAIR")
    cadastro = int(input())

    while True:  
        if cadastro == 1:
            nome = str(input("Digite seu nome: "))
            telefone = float(input("Digite seu telefone: "))
            cpf = int(input("Digite seu CPF: "))

            dados.append(nome)
            dados.append(telefone)
            dados.append(cpf)

            sair = int(input("Deseja continuar? \nSe sim - 1 \nSe não - 2 \n"))
        if sair == 2:
           break    
    break      






if cadastro == 3:
       for x in range(0,3):
          sleep(2)
          print(".")
          sleep(2)
print("Cadastro Finalizado")      