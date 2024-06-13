# conversão de tipos

idade = '24' 

print(idade, type(idade))

# Conversão explícita

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

#int()
#float()
#bool()
#str()

altura = input('Informe sua altura: ')

print(altura, type(altura))

# Por padrão o python ler o input com str. É possivel converter o valor usando alguns das funão listadas acima. Veja:

altura = float(input('Informe sua altura: '))

print(altura, type(altura))