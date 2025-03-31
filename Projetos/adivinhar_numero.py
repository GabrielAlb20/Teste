import random

def jogar():
    """Executa o jogo de adivinhar o número."""

    # Gera o número secreto
    numero_secreto = random.randint(1, 100)

    # Número máximo de tentativas
    max_tentativas = 7

    # Loop principal do jogo
    for tentativas in range(max_tentativas):
        try:
            # Obtém o palpite do jogador
            palpite = int(input("Tentativa {}: Adivinhe o número (1-100): ".format(tentativas + 1)))

            # Verifica o palpite
            if palpite == numero_secreto:
                print("Parabéns! Você acertou o número em {} tentativas.".format(tentativas + 1))
                return  # Sai do jogo
            elif palpite > numero_secreto:
                print("O número é menor.")
            else:
                print("O número é maior.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    # Se o jogador não acertar em todas as tentativas
    print("Você perdeu! O número secreto era {}.".format(numero_secreto))

# Inicia o jogo
jogar()