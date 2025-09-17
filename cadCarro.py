def carro():
    ano = int(input("Qual o ano do seu carro: "))
    cor = input("Qual a cor do seu carro: ")
    marca = input("qual a marca do seu carro: ")
    
    print("\n--- FICHA DE CADASTRO ---")
    print("Esse é o ano do seu carro: ",ano)
    print("Essa é a cor do seu carro: ",cor)
    print("Essa é a marca do seu carro:", marca)
    if ano < 2015:
        print("Seu carro é velho")
    else:
        print("Seu carro é seminovo/novo")
carro()