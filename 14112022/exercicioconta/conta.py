class Conta:
    def __init__(self, numero, tipo):
        self.__numero = numero
        self.__tipo = tipo 
        #print("Passando pelo construtor da classe Conta")
    
    def __str__(self):
        return f'O numero da sua conta é {self.__numero} e o tipo da sua conta é {self.__tipo}'
    
    