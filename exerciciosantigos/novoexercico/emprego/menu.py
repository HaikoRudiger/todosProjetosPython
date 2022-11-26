from funcoes import validacao

def empregado ():

    dicionario = {}
        
    dicionario['nome'] = str(input("Digite seu nome: "))
    dicionario['dataNascimento'] = str(input("Digite sua Data de nascimento: "))
    dicionario['numCarteiraTrabalho'] = str(input("Digite sua Data de Numero da carteira de Trabalho: "))
    
    validacao(dicionario)
    
empregado()