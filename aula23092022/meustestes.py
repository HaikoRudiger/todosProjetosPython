id = str(input("BEM-VINDO(A) AO CHATBOT!\nPor favor, digite SIM para se identificar ou NÃO para continuar: "))


# SOLICITACAO DE DADOS DO USUARIO.
if id == "sim":
    print("\nPara darmos seguimento tenha em mãos os seguintes dados: Nome completo, número de CPF e telefone")
    nome = str(input("Agora, por favor informe seu nome: "))
    cpf = input(f"Obrigado, {nome}! Agora precisamos de seu CPF. Digite apenas os números, sem pontuação: ")

    #### INCLUIR VERIFICAÇÃO DE VALIDADE DO CPF ####
    tel = int(input("Excelente, seu CPF é válido! Por último, favor digitar seu telefone para contato com DDD: "))

else:
    print("Ok, vamos continuar conversando sem identificação.")
    ### INCLUIR CADASTRO DA RECLAMACAO AQUI.