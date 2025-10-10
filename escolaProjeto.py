class Escola:
    def __init__(self,nome = None, salas = None, materias= None, banheiros = None, tamanho = None):
        self.nome = nome
        self.salas = salas
        self.materias = materias
        self.banheiros = banheiros
        self.tamanho = tamanho

    def descrever(self):
        self.nome = input("Qual o nome da escola?\n")
        self.salas = input("Quantas salas tem na escola?\n")
        self.materias = input("Quantas matérias têm?\n")
        self.banheiros = input("Quantos banheiros tem na escola?\n")
        self.tamanho = input("Qual o tamanho da escola em m²?\n")

        return f"Esta escola se chama {self.nome} tem {self.salas} salas, tem {self.materias} matérias, {self.banheiros} banheiros e {self.tamanho}m²."
es = Escola()
print(es.descrever())
    
