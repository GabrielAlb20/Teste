import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print(" Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print(" Tente um número maior")
    elif tentativa > numero_secreto:
        print(" Tente um número menor")
    else:
        print(f" Parabéns, Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break
