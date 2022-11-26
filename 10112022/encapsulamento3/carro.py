class Carro:

    def __init__(self, marca, modelo, categoria, cor):
        self._marca = marca
        self._modelo = modelo
        self._categoria = categoria 
        self._cor = cor
    
    def set_marca(self, marca):
        self._marca = marca
        
    def get_marca(self):
        return self._marca
    
    def set_modelo(self, modelo):
        self._modelo = modelo
    
    def get_modelo(self):
        return self._modelo
    
    def set_porte(self, categoria):
        self._categoria = categoria
        
    def get_categoria(self):
        return self._categoria
    
    def set_cor(self, cor):
        self.cor = cor
        
    def get_cor(self):
        return self.cor
    
    def __str__(self):
        return f'Marca: {self.get_marca} , Modelo: {self.get_modelo} , Categoria: {self.get_categoria} , Cor: {self.get_cor}'