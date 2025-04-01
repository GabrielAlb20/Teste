type([])

# Criando uma lista de números inteiros
lista1 = [6, 2, 8, 4, 38, 5, 1, 3, 7]
print(lista1)  # Exibe [1, 2, 3, 4, 5]

# Criando uma lista de strings
lista2 = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
print(lista2)  # Exibe ['G', 'F', 'E', 'D', 'C', 'B', 'A']

# Criando uma lista vazia
lista3 = []
print(lista3)  # Exibe [] (lista vazia)

# Criando uma lista com números de 0 a 10
lista4 = list(range(11))
print(lista4)  # Exibe [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista5 = list('Python')  # Converte a string 'Python' em uma lista de caracteres
print(lista5)  # Exibe ['P', 'y', 't', 'h', 'o', 'n']

# Podemos facilmente checar se detrminado elemento está na lista

if 8 in lista4:
    print('8 está na lista4')
else:
    print('8 não está na lista4')



# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)
# Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38]

# ordena uma lista de str 
lista5.sort()
print(lista5) # Exibe ['P', 'h', 'n', 'o', 't', 'y']

# podemos facilmente contr o número de ocorrencias de um valor em uma lista
print(lista1.count(8))  # Exibe 1 (o número 8 aparece uma vez na lista1)
print(lista5.count('e')) # Exibe 0 (a letra 'e' não está na lista5)

# adicionar elementos a lista
print(lista1)
"""
para adicionar elementos na lista, podemos usar os métodos append().
"""
lista1.append(42)  # Adiciona o número 42 ao final da lista1
print(lista1)

#OBS: com append, nós só conseguimos adicionar 1 elemento por vez
#se quisermos adicionar mais de um elemento, podemos usar o método extend().

lista1.append([1, 2, 3])  # Adiciona a lista [1, 2, 3] ao final da lista1
print(lista1)  # Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3]]

if [1, 2, 3] in lista1:
    print('A lista [1, 2, 3] está na lista1')
else:
    print('A lista [1, 2, 3] não está na lista1')


lista1.extend([1, 2, 3])  # Adiciona os elementos da lista [1, 2, 3] ao final da lista1 VALOR ADICIONAL
print(lista1)  # Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3]

# podemos inserir um novo elemento na lista informando a posição do índice
# OBS: isso não substitui o elemento que já está na posição, apenas adiciona um novo elemento na posição informada
# Exemplo: Adicionando o número 0 na posição 0 da lista1
lista1.insert(0, 0)  # Adiciona o número 0 na posição 0 da lista1
print(lista1)  # Exibe [0, 1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3]

# podemos facilmente juntar duas listas
# Exemplo: Juntando a lista1 e a lista2
lista6 = lista1 + lista2  # Junta a lista1 e a lista2
print(lista6)  # Exibe [0, 1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3, 'G', 'F', 'E', 'D', 'C', 'B', 'A']

# podemos facilmente inverter uma lista
# lista.reverse() inverte a lista original
lista1.reverse()  # Inverte a lista1
lista2.reverse()  # Inverte a lista2
print(lista1)  # Exibe [3, 2, 1, [1, 2, 3], 38, 8, 7, 6, 5, 4, 3, 2, 1]   

# forma 2
print(lista1[::-1])  # Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3] (inverte a lista1 sem alterar a original)
print(lista2[::-1])  # Exibe [3, 2, 1, [1, 2, 3], 38, 8, 7, 6, 5, 4, 3, 2, 1] (inverte a lista1 sem alterar a original)
print(lista1)  # Exibe [3, 2, 1, [1, 2, 3], 38, 8, 7, 6, 5, 4, 3, 2, 1] (inverte a lista1 sem alterar a original)

# copiar uma lista 
lista10 = lista2.copy() # Copia a lista2 para a lista10
print(lista10)  # Exibe ['A', 'B', 'C', 'D', 'E', 'F', 'G'] (copia a lista2 para a lista10)s
