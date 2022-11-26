lista = [[]] #lista de lista para salvar os dados

opcoes = 0 #variaveis para opção 

while opcoes != 4: 
     print ("1 - Cadastro de dados")
     print ("2 - Ver lista")
     print ("3 - Alterar cadastro")
     print ("4 - Sair")
     opcoes = int(input ())

     if opcoes == 1:        
         dados = [] #Variavel para adicionar os nomes dos cadastros
         id = str(input("Digite um ID de cadastro: "))
         nome = str(input("Digite seu nome: ")) 
         cpf = int(input("Digite seu CPF: ")) 
         dados.append(id)
         dados.append(nome)
         dados.append(cpf)
         lista.append(dados) #Colocar os dados dentro da lista de dados

     elif opcoes == 2:
          for indicarDados2 in dados:
              print(indicarDados2) 

     elif opcoes == 3:
         for indicarDados in lista:
             for indicarDados2 in dados:
                  print(indicarDados2) 
         idDados = int(input("Digite o ID do cadastro para alterar: "))
         for indicarId in range(len(id)):
             if idDados == id [indicarId] [0]:
                del(id[indicarId])

         dados = []
         id = str(input("Digite um ID de cadastro: "))
         nome = str(input("Digite seu nome: ")) 
         cpf = int(input("Digite seu CPF: ")) 
         dados.append(id)
         dados.append(nome)
         dados.append(cpf)
         lista.append(dados)



     elif opcoes == 4:
         break



print ("programa encerrado")