class Conta:
    # atributos recendo tipos
    titular = ''
    numero = 0
    saldo = 0
    limite = 0
    
    #metodo de acesso aos atributos da classe
    
    def __str__(self):
        return f'{self.titular} - {self.numero} - {self.saldo} - {self.limite}'
    
    
#MAIN

'''
from conta import Conta

conta = Conta()

conta.titular = 'Lirinha'

print(conta)
'''