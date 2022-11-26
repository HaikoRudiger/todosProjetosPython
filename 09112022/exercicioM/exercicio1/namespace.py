class Namespace:

    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    def dados(self):
        print("O numero da conta: ", self.numero, "Nome do titular: ", self.titular, "Saldo: ", self.saldo)
        
        