'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

'''
nome = input('Qual seu nome?:')
char = str(nome)

if len(char) <=4:
    print("Seu nome é curto")
elif len(char) >= 5 and len(char) <= 6:
    print("Seu nome é Normal")
else:
    print("Seu nome é muito grande")