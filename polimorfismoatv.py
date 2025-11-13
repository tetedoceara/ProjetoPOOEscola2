class Aluno:
    def estudar(self):
        print("Estudando Matemática para a prova")

class Professor:
    def estudar(self):
        print("Estudando Matemática para preparar a aula")

class Universitario:
    def estudar(self):
        print("Estudando Matemática para o TCC")

class Engenheiro:
    def estudar(self):
        print("Estudando Matemática para o projeto de engenharia")


def estudar_matematica(obj):
    obj.estudar()


a = Aluno()
p = Professor()
u = Universitario()
e = Engenheiro()

def main():
   
    objetos = [Aluno(), Professor(), Universitario(), Engenheiro()]
    for obj in objetos:
        estudar_matematica(obj)


if __name__ == "__main__":
    main()