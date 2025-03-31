#esse código pega dois valores, o primeiro que são as quantidades de dias e é dividido pela quantidade de 
#dias existente em (1) um ano.

print ("Seja bem vindo ao calculador de Dias/Anos")
print()

quan_dias = int(input("Digite a quantidade de dias :"))
media_dias_ano = 366
anos = (quan_dias / media_dias_ano)

if quan_dias >= 366:
    print(f"A quantidade de ano é",f'{anos:.2f} anos')
else:
    print('A quantidade de dias não foram suficientes para completar 1 um ano (365 dias)')



print ("Fim do Programa!")