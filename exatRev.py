class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("ERRO: Valor inválido")

produto = Produto("Notebook", 2500)

print(f"Preço: R${produto.preco}")

produto.preco = 2800
print(f"Preço atualizado: R${produto.preco}")

produto.preco = -100
print(f"Preço final: R${produto.preco}")