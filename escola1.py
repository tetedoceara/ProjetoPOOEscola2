def cadastro():
    cond = input("Digite 1 se for cadastrar um estudante, ou 2 se for cadastrar um licenciado: ")

    if cond == '1':
        print("--- FAÇA SEU CADASTRO COMO ALUNO ---")
        curso = input("Digite o curso desejado: ")
        serie = input("Digite a série desejada: ")
        nome = input("Digite seu nome: ")
        dt = input("Digite sua data de nascimento: ")
        cpf = input("Digite seu CPF: ")
        endereco = input("Digite seu endereço: ")
        dadPais = input("Digite o número do responsável: ")
        perg = input("Você tem alguma intolerância?(digite 1 para sim e 2 para não)\n")
        
        if perg == '1':
            alerg = input("Se SIM, qual?\n ")
            
        
        print("--- CADASTRO CONCLUÍDO ---")
        media = input("Deseja verificar sua média?(digite 1 para sim e 2 para não)\n")
        if media == '1':
            input("Qual é a máteria desejada? ")
            n1 = int(input("Digite a sua primeira nota: "))
            n2 = int(input("Digite a sua segunda nota: "))
            n3 = int(input("Digite a sua terceira nota: "))
            n4 = int(input("Digite a sua quarta nota: "))
            medalu = (n1 + n2 + n3 + n4)/4
            print("Essa é a sua média: ", medalu)
        if medalu >= 6:
            print("Você está aprovado(a)!!")
        else:
            print("Você está reprovado(a)!!")
        
        
    elif cond == '2':
       print("--- FAÇA SEU CADASTRO COMO PROFESSOR ---") 
       nome = input("Digite seu nome: ")
       dt = input("Digite sua data de nascimento: ")
       cpf = input("Digite seu CPF: ")
       endereco = input("Digite seu endereço: ")
       num = input("Digite seu número de contato: ")
       mat = input("Digite a máteria que é Licenciado: ")
       
       print("--- CADASTRO CONCLUÍDO ---")
       
       print("\n--------------------------")
       print("\n--- ÁREA DE CADASTRO DE NOTAS ---")

       naluno = input("Digite o nome do aluno desejado: ")
       saluno = input("Digite a série do aluno desejado: ")
       caluno = input("Digite o curso do aluno desejado: ")
       n1 = int(input("Digite a primeira nota: "))
       n2 = int(input("Digite a segunda nota: "))
       n3 = int(input("Digite a terceira nota: "))
       n4 = int(input("Digite a quarta nota: "))
       medalu = (n1 + n2 + n3 + n4)/4 
       print("O(A) aluno(a) {} do {} do curso de {} agora está com a média: {}  ".format(naluno, saluno, caluno, medalu))
       if medalu >= 6:
           print("O(A) aluno(a) está aprovado(a)!!")
       else:
           print("O(A) aluno(a) está reprovado(a)!!")    
           
def refeitorio():
    print("\n--- CARDÁPIO DO DIA ---")
    selec = input("Digite 1 para uma refeição normal\nDigite 2 para uma refeição de alérgicos e\nDigite 3 para refeição de professores:\n")
    
    if selec == '1':
        print("\n-Merenda da manhã-\nPÃO COM PATÊ E SUCO\n-Almoço-\nFRANGO TORRADO\n-Merenda da tarde-\nBOLO COM SUCO")
    elif selec == '2':
        print("\n-Merenda-\nSALADA DE FRUTAS\n-Almoço-\nOVO COZIDO\n-Merenda da tarde-\nBISCOITO SEM GLÚTEN")
    elif selec == '3':
        print("\n-Merenda da manhã-\nPÃO COM PATÊ E SUCO\n-Almoço-\nFRANGO TORRADO\n-Merenda da tarde-\nBOLO COM SUCO")

def secretaria():
    print("\n--- SECRETARIA ---")
    print("O que deseja solicitar da secretaria?")
    soli = input("Digite 1 para pedir declaração\nDigite 2 para enviar atestado:\n")
    if soli == '1':
        print("\nAqui está sua declaração:\nHGSFJSFWKSHEKQAGBFGHY")
    elif soli == '2':
        print("\nAqui o número da secretária para o envio do atestado:\n(85)987654-0934")
        
        
cadastro()
refeitorio()
secretaria()