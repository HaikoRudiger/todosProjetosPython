from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

titulo = ("="*15)

print("{} Pessoa Fisica {}".format(titulo, titulo))

pessoafisica1 = PessoaFisica(input("Digite seu titular: "), input("Digite seu CPF: "), input("Digite seu Saldo Inicial: "))



segundotitular = pessoafisica1.segundo_titular = input("Digite seu nome: ") 

print(f"O titular é {pessoafisica1.titular}, O numero do CPF é {pessoafisica1.cpf}, O saldo inicial é {pessoafisica1.saldo_inicial}, O segundo titular {segundotitular}")

print("{} Pessoa Juridica {}".format(titulo, titulo))

pessoafisica2 = PessoaJuridica(input("Digite seu titular: "), input("Digite seu CPF: "), input("Digite seu Saldo Inicial: "))



segundotitular2 = pessoafisica2.segundo_titular = input("Digite seu nome: ") 

print(f"O titular é {pessoafisica2.titular}, O numero do CNPJ é {pessoafisica2.cpf}, O saldo inicial é {pessoafisica2.saldo_inicial}, O segundo titular {segundotitular2}")

print(pessoafisica1)

print(pessoafisica2)