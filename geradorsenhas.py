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
