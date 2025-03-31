def obter_dados_usuarios():
    """
    Coleta dados do usuário
    """

    dados = {}
    dados["nome"] = input("Digite seu nome: ")
    dados["idade"] = input("Digite sua idade: ")
    dados["email"] = input("Digite seu email: ")
    dados["Cidade"] = input("Digite sua cidade: ")
    dados["Profissao"] = input("Digite sua profissão: ")

    return dados

def imprimir_dados_usuario(dados):
    """
    imprime os dados do usuário de forma organizada.
    """
    print("\n-- Dados do Usuário --")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

        # Programa principal

        if __name__ == "__main__":
            dados_usuario = obter_dados_usuarios
            imprimir_dados_usuario = (dados_usuario)