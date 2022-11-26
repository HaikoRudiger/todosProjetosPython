from funcoesgenero import cadastro, media, filtrar


dados = []

def menu():

    while True: 
        
        pessoa = {}
        print("Seu cadastro")
        pessoa['nome'] = input("Digite seu nome: ")
        pessoa['sexo'] = int(input("Digite o numero do seu genero: \n 1 - Homem \n 2 - Mulher \n 3 - Outro \n:>"))
        pessoa['idade'] = int(input("Digite sua idade: "))

        dados.append(pessoa)
        novamente = int(input("Você deseja continuar? \n 1 - Sim \n 2 - Nao \n:>"))   
        
        if novamente == 2: 
            break 
         
    while True: 
        
        opcao = int(input("Selecione a opcao que queira continuar: \n1 - Quantos Cadastro \n2 - Media \n3 - Todas as mulheres \n5 - Sair \n:>"))
            

        if opcao == 1:
            cadastro(dados)
        
        if opcao == 2: 
            media(dados)
        
        if opcao == 3: 
            filtrar(dados) 
        
        if opcao == 5:
          break
        
        
menu()