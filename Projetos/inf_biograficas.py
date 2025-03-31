def adicionar_pessoa(pessoas):
    nome = input("Digite o nome da pessoa: ")
    data_nascimento = input("Digite a data de nascimento: ")
    profissao = input("Digite a profissão: ")
    pessoas[nome] = {"data_nascimento": data_nascimento, "profissao": profissao}
    print("Pessoa adicionada com sucesso!")

def pesquisar_pessoa(pessoas):
    nome = input("Digite o nome da pessoa que você deseja pesquisar: ")
    if nome in pessoas:
        print("Informações sobre", nome + ":")
        print("Data de nascimento:", pessoas[nome]["data_nascimento"])
        print("Profissão:", pessoas[nome]["profissao"])
    else:
        print("Pessoa não encontrada.")

def listar_pessoas(pessoas):
    if pessoas:
        print("Lista de pessoas cadastradas:")
        for nome in pessoas:
            print("- " + nome)
        escolha = input("Digite o nome de uma pessoa para ver os detalhes (ou pressione Enter para voltar): ")
        if escolha in pessoas:
            pesquisar_pessoa(pessoas)
    else:
        print("Não há pessoas cadastradas.")

pessoas = {}

while True:
    print("\n--- Menu ---")
    print("1. Adicionar pessoa")
    print("2. Pesquisar pessoa")
    print("3. Listar todas as pessoas")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_pessoa(pessoas)
    elif opcao == "2":
        pesquisar_pessoa(pessoas)
    elif opcao == "3":
        listar_pessoas(pessoas)
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")