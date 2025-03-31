"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome :')
idade = input('Digite sua idade :')
espacos = ' '
print('Seu nome é', nome)
print('Seu nome invertido é', nome[::-1])
if nome == "": 
    print('Desculpe, você deixou campos vazios.')
else:
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
    print('Seu nome tem ', len(nome), 'letras')
    print('A primeira letra do seu nome é:', primeira_letra )
    print('A última letra do seu nome é :', ultima_letra )
    print('Seu nome contém espaços')

if espacos in nome:
    print('Seu nome contém espaços')
else:
    print('Seu nome não contém espaços')

   






