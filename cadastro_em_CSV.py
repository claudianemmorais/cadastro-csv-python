import csv

pessoas = []
sair = False
cabecalho = ['nome', 'email']


# Função para salvar os dados
def salvar_csv(dicionario, lista_cabecalho, arquivo):
    """ Dicionáiro para CSV """
    with open(arquivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=lista_cabecalho, delimiter=';')
        writer.writeheader()
        writer.writerows(dicionario)


# Função para ler os dados
def ler_csv(arquivo):
    """ Lê CSV e retorna uma lista com os dicionários """
    lista = []
    with open(arquivo, 'r') as file:
        csv_file = csv.DictReader(file, delimiter=';')
        for row in csv_file:
            if row:
                lista.append(dict(row))
    return lista


# Função para exibir os registros
def exibir_os_cadastrados(pessoas):
    """ Exibe na tela com formatação os dados registrados """
    # o \t gera o espaçamento de um tab
    print(f"{'N°': <5} NOME \t EMAIL")
    print('-' * 50)
    for i, pessoa in enumerate(pessoas, start=1):
        nome = pessoa['nome']
        email = pessoa['email']
        print(f"{i: <5} {nome} \t {email}")
    print('-' * 50)


# Função para adicionar um registro
def adicionar_registro(nome, email, lista):
    """ Adicionar nova pessoa a lista """
    d = {'nome': nome, 'email': email}
    lista.append(d)
    return lista


# Função para editar um registro
def editar_registro(pessoas):
    """ Edita o registro de uma pessoa """
    exibir_os_cadastrados(pessoas)
    try:
        index = int(input("\nDigite o número do registro que deseja editar: ")) - 1
        if index < 0 or index >= len(pessoas):
            print("Índice inválido!")
            return
        novo_nome = input("Digite o novo nome: ")
        novo_email = input("Digite o novo email: ")
        pessoas[index]['nome'] = novo_nome
        pessoas[index]['email'] = novo_email
        print("Registro atualizado com sucesso!")
    except ValueError:
        print("Por favor, digite um número válido.")


# Função para excluir um registro
def excluir_registro(pessoas):
    """ Exclui o registro de uma pessoa """
    exibir_os_cadastrados(pessoas)
    try:
        index = int(input("\nDigite o número do registro que deseja excluir: ")) - 1
        if index < 0 or index >= len(pessoas):
            print("Índice inválido!")
            return
        pessoas.pop(index)
        print("Registro excluído com sucesso!")
    except ValueError:
        print("Por favor, digite um número válido.")


# Função interativa do programa
def menu():
    pessoas = ler_csv("cadastro_em_CSV.csv")
    while True:
        print("\n--- Menu ---")
        print("1. Ver registros")
        print("2. Adicionar novo registro")
        print("3. Editar registro")
        print("4. Excluir registro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if pessoas:
                exibir_os_cadastrados(pessoas)
            else:
                print("Não há registros cadastrados.")

        elif opcao == '2':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            pessoas = adicionar_registro(nome, email, pessoas)
            salvar_csv(pessoas, cabecalho, "cadastro_em_CSV.csv")
            print("Cadastro realizado com sucesso!")

        elif opcao == '3':
            if pessoas:
                editar_registro(pessoas)
                salvar_csv(pessoas, cabecalho, "cadastro_em_CSV.csv")
            else:
                print("Não há registros para editar.")

        elif opcao == '4':
            if pessoas:
                excluir_registro(pessoas)
                salvar_csv(pessoas, cabecalho, "cadastro_em_CSV.csv")
            else:
                print("Não há registros para excluir.")

        elif opcao == '5':
            salvar_csv(pessoas, cabecalho, "cadastro_em_CSV.csv")
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Executando o menu
menu()

"""
# Lê os registros salvos se houver
try:
    pessoas = ler_csv("cadastro_em_CSV.csv")

except FileNotFoundError:
    print("cadastro_em_CSV.csv será gerado")

# Loop do programa
while not sair:
    if pessoas:
        exibir_os_cadastrados(pessoas)

    opcao = input("Você deseja adicionar um novo registro? (s/n): ").lower()
    if opcao == "s":
        nome = input("nome: ")
        email = input("email: ")
        pessoas = adicionar_registro(nome, email, pessoas)

    elif opcao == "n":
        r = input("sair? (s/n) ").lower()
        if r == "s":
            salvar_csv(pessoas, cabecalho, "cadastro_em_CSV.csv")
            sair = True
"""