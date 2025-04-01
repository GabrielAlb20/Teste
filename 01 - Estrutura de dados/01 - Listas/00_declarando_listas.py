# Criando uma lista de frutas e imprimindo
frutas = ["laranja", "maca", "uva"]  # Lista contendo três elementos (strings)
print(frutas)  # Exibe ['laranja', 'maca', 'uva']

# Criando uma lista vazia
frutas = []  # Lista sem elementos
print(frutas)  # Exibe []

# Criando uma lista a partir de uma string
letras = list("python")  # A função list() transforma a string em uma lista de caracteres
print(letras)  # Exibe ['p', 'y', 't', 'h', 'o', 'n']

# Criando uma lista com números de 0 a 9 usando range()
numeros = list(range(10))  # range(10) gera números de 0 a 9, e list() converte para lista
print(numeros)  # Exibe [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Criando uma lista com diferentes tipos de dados
carro = [
    "Ferrari",   # Marca do carro (string)
    "F8",        # Modelo do carro (string)
    4200000,     # Preço do carro em reais (inteiro)
    2020,        # Ano do carro (inteiro)
    2900,        # Cilindradas do motor (inteiro)
    "São Paulo", # Localização do carro (string)
    True         # Indica se o carro está disponível para venda (booleano)
]
print(carro)  
# Exibe ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]
