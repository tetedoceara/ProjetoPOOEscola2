class Pato:
    def quack(self):
        print("O  pato faz Quack!")
        
class Pessoa:
    def quack(self):
        print("A pessoa imita o som do pato: Quack!")

    def comer(self):
        print("A pessoa está comendo.")

def fazer_quack(obj):
    obj.quack()

p = Pato()
h = Pessoa()

fazer_quack(p)
fazer_quack(h)


class Gravacao:
    def quack(self):
        print("Gravação de som de pato: Quack!")

class Robo:
    def quack(self):
        print("Robo: Q-U-A-C-K! em som metálico!")  

objetos = [Pato(), Pessoa(), Gravacao(), Robo()]

for obj in objetos:
    fazer_quack(obj)  
