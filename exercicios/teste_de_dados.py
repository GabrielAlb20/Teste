name = input("qual o seu nome :")
ano_nascimento = input ("qual o ano do seu nascimento :")
ano_atual = input("qual o ano atual :")
idade = int (ano_atual) - int (ano_nascimento)
ddd = input("qual o ddd de onde você reside :")
print("olá", name, "seja bem vindo", "você nasceu no ano de", ano_nascimento, "e tem", idade, "anos", "e o ddd de onde você reside é ", ddd,) 

if idade >= 18:
      print("você é maior de idade")
else: 
      print("você é menor de idade")
if ddd == "81":
      print("pelo seu DDD, você reside no estado de Pernambuco")
elif ddd == "21":
      print("pelo seu DDD, você reside no estado do Rio de Janeiro")





