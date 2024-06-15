# > Listas

# Antes:

nota1 = 7.9
nota2 = 8.8
nota3 = 9.3
nota4 = 10

# Com listas:

lista = [7.9, 8.8, 9.3, 10]

# criando listas:

lista = [] # lista vazia.
lista = list() # função que cria um lista.

lista = [24, 'Ian', 3.14, True] # lista permite armazenar valores de vários tipos: (booleano, string, int e float)

lista_de_lista = [10, [1, 2, 3]] # lista permite armazenar outra lista dentro.

# Indexação e slices (fatiamento)

lista = [24, 'Ian', 3.14, True]

print(lista[0])  # permite acessar o elemento da lista a partir do índice, no caso, aqui está acessando elemento 24.
print(lista[-1]) # permite acessar o elemento da lista a partir do índice, no caso, aqui está acessando elemento na ordem contrária.

# slices (fatiamento)

lista = [10, 20, 30, 40, 50, 60]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[:3])
print(lista[2:6:2])

# Interação com o for:

# 1. Utilizando os próprios elementos da lista:

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices 

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])