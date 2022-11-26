from conta import Conta 

conta = Conta()

conta.titular = 'Lirinha'
conta.numero = 123456
conta.saldo = 120 
conta.limite = 1200.0

conta1 = Conta()

conta1.titular = 'Haiko'
conta1.numero = 9876554
conta1.saldo = 130 
conta1.limite = 1300.0

conta2 = Conta()

conta2.titular = 'Jean'
conta2.numero = 232323
conta2.saldo = 140 
conta2.limite = 1400.0

print(conta)
print(conta1)
print(conta2)