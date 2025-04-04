import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("🔑 Gerador de Senhas Seguras")
tamanho = int(input("Digite o tamanho da senha desejada: "))
senha = gerar_senha(tamanho)
print(f"Senha gerada: {senha}")

# CÓDIGO COMENTADO 
"""
import random   #módulo random, para gerar número aleatórios
import string   #módulo string, que tem várias constantes úteis, como letras, dígitos e pontuação

def gerar_senha(tamanho=12):  # Define uma função chamada gerar_senha, que recebe o tamanho da senha (padrão é 12 se não passar nada)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Junta letras maiúsculas e minúsculas (ascii_letters), números (digits) e símbolos (punctuation) em uma única string

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    # Gera a senha pegando um caractere aleatório da lista de caracteres, repetindo isso 'tamanho' vezes
    # ''.join(...) junta todos esses caracteres numa única string

    return senha  # Retorna a senha gerada

print("🔑 Gerador de Senhas Seguras")  # Mostra um título bonitinho no terminal

tamanho = int(input("Digite o tamanho da senha desejada: "))  
# Pede pro usuário digitar o tamanho da senha, e converte esse valor pra inteiro

senha = gerar_senha(tamanho)  # Chama a função com o tamanho informado e guarda a senha gerada

print(f"Senha gerada: {senha}")  # Exibe a senha final pro usuário



"""