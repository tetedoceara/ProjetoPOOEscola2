class Casa:
    def __init__(self, cor = None, quartos= None, banheiros = None, tamanho = None):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.tamanho = tamanho

    def descrever(self):
        self.cor = input("Qual a cor da casa?\n")
        self.quartos = input("Quantos quartos tem a casa?\n")
        self.banheiros = input("Quantos banheiros tem a casa?\n")
        self.tamanho = input("Qual o tamanho da casa em m²?\n")

        return f"Esta casa é {self.cor}, tem {self.quartos} quartos, {self.banheiros} banheiros e {self.tamanho}m²."
    
cs = Casa()
print(cs.descrever())



class Pessoa:
    def __init__(self, nome = None):
        self.nome = nome
        self.nome = input("Qual o seu nome?\n")

    def falar(self, mensagem = None):
        self.mensagem = input("O que você quer dizer?\n")
        return f"{self.nome} disse: {self.mensagem}"
    
    def cantar(self, musica = None):
        self.musica = input("Qual música você quer cantar?\n")
        return f"{self.nome} está cantando: {self.musica}"
    
    def estudar(self, materia = None):
        self.materia = input("O que você está estudando?\n")
        return f"{self.nome} está estudando: {self.materia}"
    
    def eu(self):
        return f"Meu nome é {self.nome}, e eu gostaria de falar {self.mensagem}, eu gosto de cantar a música {self.musica} e estou estudando {self.materia}."

p = Pessoa()
p.falar()
p.cantar()
p.estudar()
print(p.eu())  