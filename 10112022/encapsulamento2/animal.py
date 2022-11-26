class Animal:

    def __init__(self, especie, raca, porte, cor):
        self._especie = especie
        self._raca = raca
        self._porte = porte 
        self._cor = cor
    
    def set_especie(self, especie):
        self._especie = especie
        
    def get_especie(self):
        return self._especie
    
    def set_raca(self, raca):
        self._raca = raca
    
    def get_raca(self):
        return self._raca
    
    def set_porte(self, porte):
        self._porte = porte
        
    def get_porte(self):
        return self._porte
    
    def set_cor(self, cor):
        self.cor = cor
        
    def get_cor(self):
        return self.cor
    
    def __str__(self):
        return f'Especie: {self.get_especie} , Raça: {self.get_raca} , Porte: {self.get_porte} , Cor: {self.get_cor}'
    
    