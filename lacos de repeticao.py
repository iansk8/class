# > Laços de repetição:

# while

# Exemplo 01:

import random as rd

n = rd.randint(1, 2)

n_user = int(input('Escolha um número entre 1 e 2: '))

while n_user != n:
    print('Tente novamente...')
    n = rd.randint(1, 2)
    n_user = int(input('Escolha um número entre 1 e 2: '))
    
print('Você acertou, parabens!')

# Exemplo 02: Estrutura com contador.

contador = 0

while contador < 5:
    print(contador)
    contador += 1 

# for:

# Exemplo 01:

for i in range(10):
    print(i)

# Explorando a função range():

# Exemplo 02: com dois parâmetros:
for i in range(1, 6):
    print(i)

# Exemplo 02: com dois parâmetros:
for i in range(1, 14, 3):
    print(i)


# Exemplo prático:

sum_nota = 0

for i in range(3):
    nota = float(input(f'Informe sua nota{i}: '))
    sum_nota =+ nota

print(f'Sua média foi: {sum_nota/3}')