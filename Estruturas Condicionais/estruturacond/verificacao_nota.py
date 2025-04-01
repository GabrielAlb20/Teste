# Programa que faz a leitura de duas notas do usuário e diz se ele foi aprovado sim/não

print('Bem vindo ao calculador de notas/média')

nome = str(input('Digite seu nome: '))
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 6:
    print(nome, 'sua média foi de', media, 'você está aprovado')
elif media < 6:
    print(nome, 'sua média foi de', media, 'você está reprovado')

print("fim do programa")