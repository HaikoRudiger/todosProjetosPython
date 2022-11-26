from conta import Conta

conta = Conta(input("Digite o titular: "), input("Digite o numero: "), input("Digite o saldo: "), input("Digite o limite: "))

print(f"O titular {conta.titular}, O numero da conta {conta.numero}, O saldo da conta {conta.saldo}, O seu limite {conta.limite}")
print(conta)

conta2 = Conta(input("Digite o titular: "), input("Digite o numero: "), input("Digite o saldo: "), input("Digite o limite: "))

print(f"O titular {conta2.titular}, O numero da conta {conta2.numero}, O saldo da conta {conta2.saldo}, O seu limite {conta2.limite}")
print(conta2)