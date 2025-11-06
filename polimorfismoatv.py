class Aluno:
    def estudar(self):
        print("Estudando Matemática para a prova")

class Professor:
    def estudar(self):
        print("Estudando Matemática para preparar a aula")


def estudar_matematica(obj):
    obj.estudar()


a = Aluno()
p = Professor()

estudar_matematica(a)
estudar_matematica(p)

objetos = [Aluno(), Professor()]