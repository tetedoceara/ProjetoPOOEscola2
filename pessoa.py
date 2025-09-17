class SerVivo:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def respirar(self):
        print(f"{self.nome} está respirando...")
        
    def dormir(self):
        print(f"{self.nome} está dormindo...")
        
class Pessoa(SerVivo):
    def falar(self,mensagem):
        print(f"{self.nome} Diz: {mensagem}")
        
    def andar(self,destino):
        print(f"{self.nome} está andando até {destino}")
        
    def comer(self,comida):
        print(f"{self.nome} está comendo {comida}")

#Criando Objetos

p1 = Pessoa("Christopher Banhg", 28)
p2 = Pessoa("Lee Felix", 25)

#Chamando Objetos

p1.respirar()
p1.falar("I'm FOIVE")
p1.andar("a escola")
p1.comer("Pizza com abacaxi")

print("-----")

p2.dormir()
p2.falar("Estou estudando POO!")
