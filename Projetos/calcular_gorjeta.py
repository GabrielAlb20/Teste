def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
  """
  Calcula o valor da gorjeta com base no valor da conta e na porcentagem desejada.

  Args:
    valor_conta: O valor total da conta.
    porcentagem_gorjeta: A porcentagem da gorjeta (ex: 10 para 10%).

  Returns:
    O valor da gorjeta.
  """

  valor_gorjeta = (valor_conta * porcentagem_gorjeta) / 100
  return valor_gorjeta

# Exemplo de uso
valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print("O valor da gorjeta é: R$", valor_gorjeta)