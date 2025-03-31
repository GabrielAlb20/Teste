#Esse Código recebe dois valores e faz o calculo porcentagem e imprime para o usuário
#BONUS Adicionais cadastro de usuário + mensagem de boas vindas 
print("Seja bem vindo ao ")
print("Calculador de Porcentagem")
print()

nome = input('Digite seu nome :')

print("Seja bem vindo", nome,"!!")

pri_valor = float(input("Digite o primeiro número :")) # Ler e armazena o primeiro número digitado pelo usuário
seg_valor = float(input("Digite o segundo número :")) # Ler e armazena o segundo  número digitado pelo usuário
divi = (pri_valor / seg_valor) # faz o primeiro calculo, dividindo o os dois valores (o primeiro / o segundo)
multiplicacao = (divi * 100)   # faz o segundo calculo, com o valor dividido multiplicado por 100
# porcentagem = (multiplicacao * 100) #faz o terceiro calculo, com o valor da multiplicação

print("o Valor:", pri_valor, "é", f'{multiplicacao:.2f}', "% de ", seg_valor)