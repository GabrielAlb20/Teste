nome = 'Gabriel Gomes'
altura = 1.65
peso = 58
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Gabriel Gomes tem 1.65 de altura,
# pesa 58 quilos e seu IMC é
# 21.30