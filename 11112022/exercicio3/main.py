from pessoa import Pessoa 

pessoa = Pessoa(input("Digite seu nome: "), input("Digite seu cpf: "), input("Digite sua idade: "), input("Digite sua altura: "))

print(f'{pessoa.nome}, {pessoa.cpf}, {pessoa.idade}, {pessoa.altura}')
print(pessoa)

pessoa2 = Pessoa(input("Digite seu nome: "), input("Digite seu cpf: "), input("Digite sua idade: "), input("Digite sua altura: "))

print(f'{pessoa2.nome}, {pessoa2.cpf}, {pessoa2.idade}, {pessoa2.altura}')
print(pessoa2)