
class Conta:
    #Atributos recebendo tipos
    titular = ''
    numero = 0 
    saldo = 0 
    limite = 0
    
    def __str__(self): # self, acessar objeto #Conta
        return f'{self.titular} - {self.numero} - {self.saldo} - {self.limite}'