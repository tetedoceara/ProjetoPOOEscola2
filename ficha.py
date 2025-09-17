def cadastro():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    endereco = input("Digite seu endereço: ")
    email = input("Digite o seu e-mail: ")
    idade = int(input("Digite a sua idade: "))
    
    
    print("\n--- FICHA DE CADASTRO ---")
    print("meu nome é: ", nome)
    print("meu cpf é: ", cpf)
    print("minha idade é: ",idade)
    print("meu endereço é: ", endereco)
    print("meu e-mail é: ",email)
    
    if idade < 18:
        print("Você é menor de idade, não pode se cadastrar :)")
    else:
        print("Você é maior de idade \n Cadastro realizado com sucesso!")
cadastro()

    
    
    
