# > Laços de repetição:

import random as rd

n = rd.randint(1, 2)

n_user = int(input('Escolha um número entre 1 e 2: '))

while n_user != n:
    print('Tente novamente...')
    n = rd.randint(1, 2)
    n_user = int(input('Escolha um número entre 1 e 2: '))
    
print('Você acertou, parabens!')