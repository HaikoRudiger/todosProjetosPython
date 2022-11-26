from conta import Conta 

class PessoaFisica(Conta):
    
    __segundo_titular = " "
    
    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__("Putz",  )
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial
        