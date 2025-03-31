import random

def jogar():
    """Executa uma rodada do jogo Pedra, Papel e Tesoura."""

    # Opções do jogo
    opcoes = ["pedra", "papel", "tesoura"]

    # Escolha do usuário
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    while escolha_usuario not in opcoes:
        escolha_usuario = input("Escolha inválida. Escolha pedra, papel ou tesoura: ").lower()

    # Escolha do computador
    escolha_computador = random.choice(opcoes)

    # Mostra as escolhas
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_computador)

    # Escolhe o vencedor
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra"):
        print("Você ganhou!")
    else:
        print("O computador ganhou!")



# Inicia o jogo
while True:
    jogar()
    jogar_novamente = input("Jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        break

    #pretendo aprimorar o jogo, colocando rounds na "partida", por exemplo: 3 rounds, e ver quem ganha, a máquina ou o usuário.
