'''
Interpolação basica de Strings
s - String
d e i - Int
f - float
x e X  - Hexadecimal (ABCDEF0123456789)

'''

nome = "Gildevan"
valor = 1.350

salario = '%s Seu salário será de R$%.3f' % (nome,valor)
print(salario)