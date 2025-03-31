string = "Python é uma linguagem poderosa"

# Fatiar do início até o índice 6 (exclusivo)
print(string[0:6])  # Saída: Python

# Fatiar do índice 7 até o final
print(string[7:])   # Saída: é uma linguagem poderosa

# Fatiar do índice 0 até o 6, com passo 2
print(string[0:6:2]) # Saída: Pto

# Fatiar do índice 7 até o 11
print(string[7:11])  # Saída: é um

# Fatiar do final até o início (invertendo a string)
print(string[::-1])  # Saída: arosodop megaugnil amu é nohTyP

# Fatiar os últimos 8 caracteres
print(string[-8:])  # Saída: poderosa

# Fatiar do 10º caracter até o 5º, com passo -1 (de trás para frente)
print(string[10:5:-1]) # Saída: agneu

# Fatiar toda a string (cópia)
print(string[:])   # Saída: Python é uma linguagem poderosa