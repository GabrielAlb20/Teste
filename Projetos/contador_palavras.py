def contar_palavras(texto):
  """
  Conta o número de palavras em um texto.

  Args:
    texto: O texto a ser analisado.

  Returns:
    Um dicionário onde as chaves são as palavras e os valores são suas contagens.
  """

  palavras = texto.lower().split()  # Converte para minúsculas e divide em palavras
  contagem = {}
  for palavra in palavras:
    if palavra in contagem:
      contagem[palavra] += 1
    else:
      contagem[palavra] = 1
  return contagem

# Exemplo de uso
texto = "Este é um exemplo de texto para contar as palavras. Este texto tem algumas palavras repetidas."
resultado = contar_palavras(texto)
print(resultado)