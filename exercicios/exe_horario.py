'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
try:

 hora = int(input('Digite a hora atual :'))

 if 0 <= hora <=11:
    print('Olá, Bom dia!')
 elif 12 <= hora <= 17:
    print('Olá, Boa tarde')
 elif 17 <= hora <= 23:
    print('Olá, boa noite!')
 else:
    print('Hora inválida, por favor digite um valor entre 0 e 23')

except ValueError:
  print('Informe apenas números com dois dígitos')