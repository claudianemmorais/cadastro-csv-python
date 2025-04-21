import csv

pessoas = []
sair = False
cabecalho = ['nome', 'email']


def salvar_csv(dicionario, lista_cabecalho, arquivo):
    """ Dicionáiro para CSV """
    with open(arquivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=lista_cabecalho, delimiter=';')
        writer.writeheader()
        writer.writerows(dicionario)


def ler_csv(arquivo):
    """ Lê CSV e retorna uma lista com os dicionários """
    lista = []
    with open(arquivo, 'r') as file:
        csv_file = csv.DictReader(file, delimiter=';')
        for row in csv_file:
            if row:
                lista.append(dict(row))
    return lista


def exibir_os_cadastrados(pessoas):
    """ Exibe na tela com formatação os dados registrados """
    # o \t gera o espaçamento de um tab
    print('NOME \t EMAIL')
    for pessoa in pessoas:
        nome = pessoa['nome']
        email = pessoa['email']
        print(f'{nome} \t {email}')


def adicionar_registro(nome, email, lista):
    """ Adicionar nova pessoa a lista """
    d = {'nome': nome, 'email': email}
    lista.append(d)
    return lista


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
