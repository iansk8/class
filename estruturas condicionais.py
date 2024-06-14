# > Estruturas condicionais

idade = float(input('Qual a sua idade? '))

if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Voceê é menor de idade!')

"""
    - Imagine que você queira imprimir "Aprovado(a)", caso o estudande tenha uma média superior ou igual a 7, e, "Reprovado", caso a média seja inferior a 7.
"""

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2)/2 
presenca = 100

if media >= 7:
    print(f'Sua mé dia foi: {media}. Você está aprovado(a)!')
elif media >= 5:
    print(f'Sua média foi: {media}. Você está na recuperação!')
else:
    print(f'Sua média foi: {media}. Você está reprovado(a)!')

# Outro exemplo: podemos fazer estruturas condicionais compostas usando "and" e "or":

if media >= 7 and presenca > 70:
    print(f'Sua mé dia foi: {media}. Você está aprovado(a)!')
elif media >= 5 and presenca > 70:
    print(f'Sua média foi: {media}. Você está na recuperação!')
else:
    print(f'Sua média foi: {media}. Você está reprovado(a)!')
