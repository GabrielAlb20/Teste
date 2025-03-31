def mad_libs():
    """Cria um jogo Mad Libs interativo."""

    print("Bem-vindo ao Mad Libs!")

    # Coleta as palavras do usuário
    adjetivo = input("Digite um adjetivo: ")
    verbo = input("Digite um verbo: ")
    substantivo = input("Digite um substantivo: ")
    advérbio = input("Digite um advérbio: ")
    lugar = input("Digite um lugar: ")
    nome = input("Digite um nome: ")
    objeto = input("Digite um objeto: ")


    # Cria a história Mad Lib
    historia = f"Era uma vez, em um dia {adjetivo}, um {substantivo} decidiu {verbo} {advérbio} em {lugar}.  De repente, {nome} apareceu segurando um {objeto}! Que aventura!"

    # Exibe a história
    print("\nSua história Mad Libs:\n")
    print(historia)


# Inicia o jogo
mad_libs()


# Outra versão com mais opções de história e mais palavras para coletar:

def mad_libs_plus():
    print("Bem-vindo ao Mad Libs Plus!")

    # Coleta as palavras do usuário
    adjetivo1 = input("Digite um adjetivo: ")
    adjetivo2 = input("Digite outro adjetivo: ")
    verbo1 = input("Digite um verbo: ")
    verbo2 = input("Digite outro verbo: ")
    substantivo1 = input("Digite um substantivo: ")
    substantivo2 = input("Digite outro substantivo: ")
    advérbio = input("Digite um advérbio: ")
    lugar = input("Digite um lugar: ")
    nome = input("Digite um nome: ")
    objeto = input("Digite um objeto: ")
    plural = input("Digite um substantivo no plural: ")


    # Escolhe uma história aleatoriamente (você pode adicionar mais)
    import random

    historias = [
        f"Um {adjetivo1} {substantivo1} estava {verbo1} {advérbio} em {lugar} quando viu um {adjetivo2} {substantivo2}. {nome} ficou chocado ao ver que o {substantivo2} estava segurando {plural} e tentando {verbo2} um {objeto}!",
        f"No meio da noite, um {adjetivo1} {substantivo1} acordou com um barulho.  {nome} saiu da cama e viu um {adjetivo2} {substantivo2} {verbo1} {advérbio} pela janela.  O {substantivo2} estava tentando roubar {plural}!",
        f"Era uma vez, em um reino distante, havia um {adjetivo1} {substantivo1} que adorava {verbo1} {advérbio}. Um dia, {nome} encontrou um {adjetivo2} {substantivo2} perdido em {lugar}.  O {substantivo2} estava procurando por seus {plural}."
    ]

    historia_escolhida = random.choice(historias)

    print("\nSua história Mad Libs Plus:\n")
    print(historia_escolhida)

# Inicia o jogo Plus (se quiser jogar essa versão)
# mad_libs_plus()  # Descomente para executar a versão plus