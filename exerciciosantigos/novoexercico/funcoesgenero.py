def cadastro(dados):
    print(f"Foram cadastrados {len(dados)} pessoas") # len(varivel) = mostrar a quantidade de dados haiko = 5

def media(dados):
    idade = 0
    for pessoa in dados: # lendo linha por linha em dados
        idade += pessoa['idade'] # adicionando idade em na variavel idade
    print(f"A media é {idade/len(dados):.1f}") # aqui pegando idade com a quantidade de dados com o len(), fazendo a divisao para achar a media   
    # [{'nome': 'haiko', 'sexo': '1', 'idade': 22}, {'nome': 'marcos', 'sexo': '2', 'idade': 99}]
    
    
def filtrar(dados):
    
    filtro = lambda x: x['sexo'] == 2  #LAMBDA: Função anonima,  função que o usuário não precisa definir, não vai precisar escrever a função e depois utilizá-la dentro do código
    #filtro está definindo com uma função anonima = x que so o numero 2 em sexo ira ser filtrada
    
    filtrados = list(filter(filtro, dados))
    #varialvel filtrados está definindo que filter, vai filtrar os dados com a outra variavel definida 'filtro' 
    #A função list() cria um objeto de lista . Um objeto de lista é uma coleção que é ordenada e mutável
    print(f"{filtrados}\n")
    
    
    
