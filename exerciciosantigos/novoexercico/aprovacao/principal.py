from funcao import media

def menu():
    
    dados = {}
    
    dados['nome'] = str(input("Digite seu nome: "))
    dados['nota1'] = float(input("Digite sua primeira nota: "))
    dados['nota2'] = float(input("Digite sua segunda nota: "))
    dados['nota3'] = float(input("Digite sua terceira nota: "))
    
    media(dados)

menu()
    
    