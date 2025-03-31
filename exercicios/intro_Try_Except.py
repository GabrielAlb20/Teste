try:
    numero1 = int(input('Digite o primeiro número :'))
    numero2 = int(input('Digite o segundo número: '))
    resultado = numero1 / numero2
    print('O resultado da divisão é: ', resultado)

except ZeroDivisionError:
    print('Erro: Divisão por zero não permitida.')
except ValueError:
    print('Erro: Entrada inválida. Digite apenas números.')
else:
    print('Divisão realizada com sucesso!')
finally:
    print('Fim do bloco try-except.')

print('O programa continua a execução após o tratamento das exceção.')

'''
try: O código dentro do bloco try é o que pode potencialmente gerar uma exceção (no caso, ZeroDivisionError ou ValueError).

except ZeroDivisionError: Se ocorrer uma exceção do tipo ZeroDivisionError (divisão por zero), o código dentro deste bloco except será executado.

except ValueError: Se ocorrer uma exceção do tipo ValueError (quando o usuário digita algo que não pode ser convertido para um inteiro),

o código dentro deste bloco except será executado.

Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.

else: O bloco else é executado somente se nenhuma exceção ocorrer dentro do bloco try.

finally: O bloco finally é sempre executado, independentemente de ter ocorrido ou não uma exceção.

É útil para código de limpeza, como fechar arquivos ou conexões com bancos de dados.
'''