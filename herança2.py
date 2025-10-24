from typing import Optional
class Pessoa:
    def __init__(self, nome: None, cpf: None, matricula: None) -> None:
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula

    def apresentar(self) -> str:
        nome = self.nome or "<sem nome>"
        cpf = self.cpf or "<sem CPF>"
        return f"Olá, meu nome é {nome} e meu CPF é {cpf}."


class Aluno(Pessoa):
    def __init__(self, nome: None, matricula: None, cpf:None) -> None:
        
        if nome is None:
            nome = input("Digite o nome do aluno: ")
        if matricula is None:
            matricula = input("Digite a matrícula do aluno: ")
        if cpf is None:
            cpf = input("Digite o CPF do aluno: ")
            
        super().__init__(nome, cpf, matricula)
        self.matricula = matricula

    def apresentar(self) -> str:
        nome = self.nome or "<sem nome>"
        cpf = self.cpf or "<sem CPF>"
        matricula = self.matricula or "<sem matrícula>"
        return f"Olá, meu nome é {nome} meu cpf é {cpf} e minha matrícula é {matricula}."


class Professor(Pessoa):
    def __init__(self, nome: None, disciplina: None, matricula: None) -> None:
        # Se algum campo não for fornecido, pede via input (mantendo a ideia original)
        if nome is None:
            nome = input("Digite o nome do professor: ")
        if disciplina is None:
            disciplina = input("Digite a disciplina que o professor ensina: ")
        if matricula is None:
            matricula = input("Digite a matricula do professor: ")

        # Professor não fornece CPF aqui; passa None para o parâmetro cpf
        super().__init__(nome, None, matricula)
        self.disciplina = disciplina

    def apresentar(self) -> str:
        nome = self.nome or "<sem nome>"
        matricula = self.matricula or "<sem matrícula>"
        disciplina = self.disciplina or "<sem disciplina>"
        return f"Olá, meu nome é {nome} minha matricula é {matricula} e eu ensino {disciplina}."


class BolsaMixin:
    def calcular_bolsa(self) -> float:
        return 1200.0 


class AlunoBolsista(BolsaMixin, Aluno):
    def __init__(self, nome: None, matricula:  None, cpf: None) -> None:
        super().__init__(nome, matricula, cpf)

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e recebo bolsa de R${self.calcular_bolsa():.2f}."


def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
    return [pessoa.apresentar() for pessoa in pessoas]


def main() -> None:
    p = Pessoa("João", "000.000.000-00")
    a = Aluno()
    prof = Professor()
    ab = AlunoBolsista("Beatriz", "B456", "333.333.333-33")

    resultados = apresentar_todos([p, a, prof, ab])
    for r in resultados:
        print(r)

    print("",
          f"isinstance(ab, Pessoa): {isinstance(ab, Pessoa)}",
          f"isinstance(ab, Aluno): {isinstance(ab, Aluno)}",
          f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}",
          sep="\n")

    print("MRO AlunoBolsista:")
    for cls in AlunoBolsista.__mro__:
        print(" -", cls.__name__)


if __name__ == "__main__":
    main()
