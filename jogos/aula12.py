print("Calculador de IMC")

nome = str(input("digite seu nome :"))
altura = float(input("digite sua altura :"))
peso = int(input("digite seu peso :"))
imc = peso / (altura**2)
print(f'{nome} tem {altura} de altura e o seu IMC é {imc}')

