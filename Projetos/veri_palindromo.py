# Usando recursão:
def eh_palindromo_recursivo(texto):
  """
  Verifica se uma string é um palíndromo usando recursão.

  Args:
    texto: A string a ser verificada.

  Returns:
    True se a string for um palíndromo, False caso contrário.
  """

  # Converte a string para minúsculas e remove espaços em branco e pontuação.
  texto = texto.lower()
  texto = ''.join(caractere for caractere in texto if caractere.isalnum())

  # Caso base:
  if len(texto) <= 1:
    return True

  # Caso recursivo:
  if texto[0] == texto[-1]:
    return eh_palindromo_recursivo(texto[1:-1])
  else:
    return False

# Usando um loop for:
def eh_palindromo_loop(texto):
  """
  Verifica se uma string é um palíndromo usando um loop for.

  Args:
    texto: A string a ser verificada.

  Returns:
    True se a string for um palíndromo, False caso contrário.
  """

  # Converte a string para minúsculas e remove espaços em branco e pontuação.
  texto = texto.lower()
  texto = ''.join(caractere for caractere in texto if caractere.isalnum())

  # Compara a string com sua versão invertida.
  for i in range(len(texto) // 2):
    if texto[i] != texto[-i - 1]:
      return False

  return True