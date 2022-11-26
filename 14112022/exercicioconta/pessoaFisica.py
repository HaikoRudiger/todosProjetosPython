from conta import Conta

class PessoaFisica(Conta):
    
    __segundo_titular = ""
    
        
    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__("Não sei", "f")
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial    
        #print("Passando pelo construtor da classe PessoaFisica")
    
    @property 
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
     
    def __str__(self):
        return f'{super().__str__()} \n  O titular da conta é {self.titular} O cpf é {self.cpf} O saldo inicial é {self.saldo_inicial}'