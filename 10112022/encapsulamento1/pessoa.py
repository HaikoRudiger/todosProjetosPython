class Pessoa:
    
    def __init__(self, nome, cpf, idade, altura):
        self._nome = nome 
        self._cpf = cpf 
        self._idade = idade
        self._altura = altura   
    
    def set_nome(self, nome):     
        self._nome = nome
    
    def get_nome(self):
        return self._nome 
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_cpf(self):
        return self._cpf
    
    def set_idade(self, idade):
        self._idade = idade
        
    def get_idade(self):
        return self._idade
    
    def set_altura(self, altura):
        self._altura = altura
        
    def get_altura(self):
        return self._altura
    
    def __str__(self):
        return f'Seu nome é {self.get_nome()} \n Seu CPF é {self.get_cpf()} \n Sua idade é {self.get_idade()} \n Sua altura é {self.get_altura()}'
    
    