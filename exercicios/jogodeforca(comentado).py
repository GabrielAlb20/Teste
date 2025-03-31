import random

# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    """Retorna uma palavra aleatória da lista de palavras."""
    palavras = ["carro","viagem", "escritor", "sonhar", "jaqueta", "floresta", "zero", "primeiro"]
    return random.choice(palavras)

# Função para exibir o estado atual do jogo
def exibir_estado_atual(letras_certas, tentativas_restantes, letras_tentadas):
    """Exibe o estado atual do jogo, incluindo as letras corretas, tentativas restantes e letras já tentadas."""
    print(f"\nTentativas restantes: {tentativas_restantes}")
    print(f"Letras já tentadas: {', '.join(letras_tentadas)}")
    print("Palavra:", " ".join(letras_certas))

# Função para verificar se o jogo terminou
def verificar_fim_de_jogo(letras_certas, tentativas_restantes):
    """Verifica se o jogador ganhou ou perdeu o jogo."""
    if "_" not in letras_certas:
        print("Parabéns! Você adivinhou a palavra!")
        return True
    elif tentativas_restantes <= 0:
        print("Você perdeu! Suas tentativas acabaram.")
        return True
    return False

# Função principal do jogo da forca
def jogo_da_forca():
    """Implementa a lógica principal do jogo da forca."""
    palavra_secreta = escolher_palavra()  # Escolhe a palavra secreta
    tentativas_restantes = 6  # Define o número de tentativas
    letras_certas = ["_"] * len(palavra_secreta)  # Inicializa a lista de letras corretas
    letras_tentadas = []  # Inicializa a lista de letras já tentadas

    # Loop principal do jogo
    while tentativas_restantes > 0 and "_" in letras_certas:
        # Obtém a entrada do usuário e valida
        letra = input("Digite uma letra: ").lower()
        while len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Adiciona a letra à lista de letras tentadas
        letras_tentadas.append(letra)

        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:
            # Atualiza a lista de letras corretas
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_certas[i] = letra
            print("Correto!")
        else:
            print("Incorreto!")
            tentativas_restantes -= 1

        # Exibe o estado atual do jogo
        exibir_estado_atual(letras_certas, tentativas_restantes, letras_tentadas)

        # Verifica se o jogo terminou
        if verificar_fim_de_jogo(letras_certas, tentativas_restantes):
            break

# Executa o jogo da forca
if __name__ == "__main__":
    jogo_da_forca()