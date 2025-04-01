# Verificação de idade, utilizando estrutura condicionais 

print('Verficador de fases da idade humana')

nome = str(input('Digite seu nome :'))
print('seja bem vindo', nome,"!")
idade = int(input("Digite sua idade :"))

'''' 
if idade <= 1:
    print('está na categoria de recém nascido')
else:
    if idade >=13:
        print('está na categoria de criança')
    else:
        if idade >=18:
            print('está na categoria de de adolescente')
        else:
            if idade >=60:
                print('está na cetegoria de idoso')
            else:
                if idade >=80:
                    print('está na categoria de Longevo')

 esse método faz deslocar excessivamente os blocos á direita, então não utilizaremos ela, iremos utilizar o comando ELIF.'''

         
if idade <=1:
    print ('Recém nascido')
elif idade < 13:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
elif idade <80:
    print('Idoso')
elif idade >80:
    print('Longevo')

print("FIM DO PROGRAMA")