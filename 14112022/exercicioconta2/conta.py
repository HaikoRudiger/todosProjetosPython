
class Conta:
    def __init__(self, numero, agencia , tipo):
        self.__numero = numero 
        self.__agencia = agencia
        self.__tipo = tipo 
        print("Passando pelo construtor da classe Conta")
        
    def __str__(self):
        return f'O numero da conta é {self.__numero} A agencia é {self.__agencia} O tipo da conta é {self.__tipo}'
    
    