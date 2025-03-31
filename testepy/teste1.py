import random
# tente adivinhar o número aleatório entre 1 e 200	

numero_aleatorio = random.randint(1, 200)
tentativas = 0
print("Tente adivinhar o número entre 1 e 200")
while True:
    if tentativas == 0:
        print('Digite seu palpite:')
    else:
        print('Digite seu palpite novamente:')
    tentativas += 1
    palpite = int(input())
    if palpite < numero_aleatorio:
        print('Tente um número maior')
    elif palpite > numero_aleatorio:
        print('Tente um número menor')
    else:   
        print(f'Parabéns, você acertou o número {numero_aleatorio} em {tentativas} tentativas')
        break
# fim do jogo

