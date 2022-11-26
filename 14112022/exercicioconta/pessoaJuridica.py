from conta import Conta

class PessoaJuridica(Conta):
    
    __segundo_titular = " "
    
    def __init__(self, titular, cnpj, saldo_inicial):
        super().__init__("Boa pergunta", "essa eu n sei")
        self.titular = titular
        self.cnpj = cnpj 
        self.saldo_inicial = saldo_inicial 
        #print("Passando pelo construtor da classe Pessoa Fisica")
        
    @property
    def segundo_titular(self):
        return self.__segundo_titular 
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
    
    def __str__(self):
        return f'{super().__str__()} \n O titular da conta é {self.titular} \n O cnpj é {self.cnpj} \n O saldo inicial é {self.saldo_inicial}'