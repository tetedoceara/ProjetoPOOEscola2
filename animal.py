class  Animal:
    def __init__(self, nome):
        self.nome = nome 
    def falar(self):
        print("Som do animal")

class Cachorro(Animal):
    def falar(self):
        print("au au!")

class Gato(Animal):
    def falar(self):
        print("miau miau...")
        
class  Pessoa:
    def __init__(self,nome):
        self.nome = nome
    def bater(self):
        print("BAH!!")
        

dog = Cachorro("Doguinho do grau")
cat = Gato("Shakira")

dog.falar()
cat.falar()
