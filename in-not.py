# Operdadores in e not in
# IN significa não entre e not não entre
#Strings são interáveis 
# 0.1.2.3.4.5.6.7
# G.i.l.d.e.v.a.n
#-6.-5.-4.-3.-2.-1
# nome = "Gildevan"
# print(nome[0])
# print(nome[1])
# print(nome[2])
# print(nome[3])
# print(nome[4])
# print(nome[5])
# print(nome[6])
# print(nome[7])
# print(nome[-8])

# print('Gild'in nome)
# print('s'in nome)

print( 10 * "-")

nome1 = input("Digite seu nome:\n")
encontar = input(f"O que deseja encontrar {nome1}:\n")
if encontar in nome1:
    print(f"{encontar} está em {nome1}")
else:
    print(f"Não está en {nome1}")
