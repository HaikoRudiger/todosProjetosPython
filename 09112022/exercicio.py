class Conta:
    numeros = 0 
    titular = ''
    saldo = 0 
    limite = 0
    
    def __str__(self):
        return f'{self.numeros} - {self.titular} - {self.saldo} - {self.limite}'