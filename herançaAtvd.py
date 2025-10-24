class Animal:
    def __init__(self, cor=None, peso=None, tamanho=None, raca=None, sexo=None):
        self.cor = cor
        self.peso = peso
        self.tamanho = tamanho
        self.raca = raca
        self.sexo = sexo

class Gato(Animal):
    def __init__(self, cor=None, peso=None, tamanho=None, raca=None, vacina=None, nome=None, sexo=None):
        if cor is None:
            cor = input("Digite a cor do gato: ")
        if peso is None:
            peso = input("Digite o peso do gato: ")
        if tamanho is None:
            tamanho = input("Digite o tamanho do gato: ")
        if raca is None:
            raca = input("Digite a raça do gato: ")
        if sexo is None:
            sexo = input("Digite o sexo do gato: ")
        if vacina is None:
            vacina = input("O gato está vacinado? ")
        if nome is None:
            nome = input("Digite o nome do gato: ")
        super().__init__(cor, peso, tamanho, raca, sexo)
        self.vacina = vacina
        self.nome = nome

    def apresentar(self):
        nome = self.nome or "<sem nome>"
        raca = self.raca or "<sem raça>"
        peso = self.peso or "<sem peso>"
        tamanho = self.tamanho or "<sem tamanho>"
        cor = self.cor or "<sem cor>"
        vacina = self.vacina or "<sem dados de vacina>"
        sexo = self.sexo or "<sem sexo>"

        return f"Oi, o nome do(a) gato(a) é {nome}, a raça dele(a) é {raca}, ele(a) pesa {peso}kg, tem {tamanho}cm, a cor dele(a) é {cor}, e ele(a) é do sexo {sexo}, e está ou não vacinado: {vacina}"

class Cachorro(Animal):
    def __init__(self, cor=None, peso=None, tamanho=None, raca=None, vacina=None, nome=None, sexo=None):
        if cor is None:
            cor = input("Digite a cor do cachorro: ")
        if peso is None:
            peso = input("Digite o peso do cachorro: ")
        if tamanho is None:
            tamanho = input("Digite o tamanho do cachorro: ")
        if raca is None:
            raca = input("Digite a raça do cachorro: ")
        if sexo is None:
            sexo = input("Digite o sexo do cachorro: ")
        if vacina is None:
            vacina = input("O cachorro está vacinado? ")
        if nome is None:
            nome = input("Digite o nome do cachorro: ")
        super().__init__(cor, peso, tamanho, raca, sexo)
        self.vacina = vacina
        self.nome = nome

    def apresentar(self):
        nome = self.nome or "<sem nome>"
        raca = self.raca or "<sem raça>"
        peso = self.peso or "<sem peso>"
        tamanho = self.tamanho or "<sem tamanho>"
        cor = self.cor or "<sem cor>"
        vacina = self.vacina or "<sem dados de vacina>"
        sexo = self.sexo or "<sem sexo>"

        return f"Oi, o nome do(a) cachorro(a) é {nome}, a raça dele(a) é {raca}, ele(a) pesa {peso}kg, tem {tamanho}cm, a cor dele(a) é {cor}, e ele(a) é do sexo {sexo}, e está ou não vacinado: {vacina}"

class Passaro(Animal):
    def __init__(self, cor=None, peso=None, tamanho=None, raca=None, nome=None, sexo=None, vacina=None):
        if cor is None:
            cor = input("Digite a cor do pássaro: ")
        if peso is None:
            peso = input("Digite o peso do pássaro: ")
        if tamanho is None:
            tamanho = input("Digite o tamanho do pássaro: ")
        if raca is None:
            raca = input("Digite a raça do pássaro: ")
        if sexo is None:
            sexo = input("Digite o sexo do pássaro: ")
        if vacina is None:
            vacina = input("O pássaro está vacinado? ")
        if nome is None:
            nome = input("Digite o nome do pássaro: ")
        super().__init__(cor, peso, tamanho, raca, sexo)
        self.nome = nome
        self.vacina = vacina

    def apresentar(self):
        nome = self.nome or "<sem nome>"
        raca = self.raca or "<sem raça>"
        peso = self.peso or "<sem peso>"
        tamanho = self.tamanho or "<sem tamanho>"
        cor = self.cor or "<sem cor>"
        vacina = self.vacina or "<sem dados de vacina>"
        sexo = self.sexo or "<sem sexo>"

        return f"Oi, o nome do(a) pássaro é {nome}, a raça dele(a) é {raca}, ele(a) pesa {peso}kg, tem {tamanho}cm, a cor dele(a) é {cor}, e ele(a) é do sexo {sexo}, e está ou não vacinado: {vacina}"
    
class Peixe(Animal):
    def __init__(self, cor=None, peso=None, tamanho=None, raca=None, nome=None, sexo=None, vacina=None):
        if cor is None:
            cor = input("Digite a cor do peixe: ")
        if peso is None:
            peso = input("Digite o peso do peixe: ")
        if tamanho is None:
            tamanho = input("Digite o tamanho do peixe: ")
        if raca is None:
            raca = input("Digite a raça do peixe: ")
        if sexo is None:
            sexo = input("Digite o sexo do peixe: ")
        if vacina is None:
            vacina = input("O peixe está vacinado? ")
        if nome is None:
            nome = input("Digite o nome do peixe: ")
        super().__init__(cor, peso, tamanho, raca, sexo)
        self.nome = nome
        self.vacina = vacina

    def apresentar(self):
        nome = self.nome or "<sem nome>"
        raca = self.raca or "<sem raça>"
        peso = self.peso or "<sem peso>"
        tamanho = self.tamanho or "<sem tamanho>"
        cor = self.cor or "<sem cor>"
        sexo = self.sexo or "<sem sexo>"
        vacina = self.vacina or "<sem dados de vacina>"

        return f"Oi, o nome do(a) peixe é {nome}, a raça dele(a) é {raca}, ele(a) pesa {peso}kg, tem {tamanho}cm, a cor dele(a) é {cor}, e ele(a) é do sexo {sexo}, e está ou não vacinado: {vacina}"
    
class Outro(Animal):
    def __init__(self, cor=None, peso=None, tamanho=None, raca=None, nome=None, sexo=None, tipo=None, vacina=None):
        if tipo is None:
            tipo = input("Digite a espécie do animal: ")
        if cor is None:
            cor = input("Digite a cor do animal: ")
        if peso is None:
            peso = input("Digite o peso do animal: ")
        if tamanho is None:
            tamanho = input("Digite o tamanho do animal: ")
        if raca is None:
            raca = input("Digite a raça do animal: ")
        if sexo is None:
            sexo = input("Digite o sexo do animal: ")
        if vacina is None:
            vacina = input("O animal está vacinado? ")
        if nome is None:
            nome = input("Digite o nome do animal: ")
        super().__init__(cor, peso, tamanho, raca, sexo)
        self.nome = nome
        self.vacina = vacina
        self.tipo = tipo

    def apresentar(self):
        nome = self.nome or "<sem nome>"
        tipo = self.tipo or "<sem tipo>"
        raca = self.raca or "<sem raça>"
        peso = self.peso or "<sem peso>"
        tamanho = self.tamanho or "<sem tamanho>"
        cor = self.cor or "<sem cor>"
        sexo = self.sexo or "<sem sexo>"
        vacina = self.vacina or "<sem dados de vacina>"

        return f"Oi, seu animal é um(uma) {tipo}, o nome do(a) animal é {nome}, a raça dele(a) é {raca}, ele(a) pesa {peso}kg, tem {tamanho}cm, a cor dele(a) é {cor}, e ele(a) é do sexo {sexo}, e está ou não vacinado: {vacina}"

def apresentar_todos(animais):
    return [animal.apresentar() for animal in animais]


def escolher_animal():
    prompt = (
        "Digite qual é o animal que você deseja cadastrar:\n"
        "1 - Gato\n"
        "2 - Cachorro\n"
        "3 - Pássaro\n"
        "4 - Peixe\n"
        "5 - Outro\n"
    )
    while True:
        esc = input(prompt).strip()
        if esc == "1":
            return Gato()
        elif esc == "2":
            return Cachorro()
        elif esc == "3":
            return Passaro()
        elif esc == "4":
            return Peixe()
        elif esc == "5":
            return Outro()
        else:
            print("Opção inválida. Tente novamente.")

def main():
    animais = []
    try:
        n = int(input("Quantos animais deseja cadastrar? "))
    except Exception:
        n = 1

    for _ in range(n):
        animais.append(escolher_animal())

    resultados = apresentar_todos(animais)
    for r in resultados:
        print(r)


if __name__ == "__main__":
    main()
