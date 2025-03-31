# pega dois valores e faz diferente operações aritiméticas de acordo com o desejo do usuário

print("Bem vindo a Calculadora Python")

print("As opções disponíveis são")
print(" 1= SOMA   2= SUBTRAÇÃO  3 =MULTIPLICAÇÃO 4 =DIVISÃO")

opcoes = int(input("Digite uma opção 1/2/3/4 :"))
prime_number = float(input("Digite o primeiro número: "))
second_number = float(input("Digite o segundo número: "))


if opcoes == 1:
    print ("a soma é : ", prime_number + second_number)
elif opcoes == 2:
    print("a subtração é : ", prime_number - second_number)
elif opcoes == 3:
    print("a multiplicação é : ", prime_number * second_number)
elif opcoes == 4:
    print("a divisão é :",prime_number / second_number)
else:
    print("Voce não digitou um número válido!")
    print("Tente novamente com uma das opções disponíveis")