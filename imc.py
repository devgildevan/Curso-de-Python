nome = str("Érkia")
altura = float(1.80)
peso = int(95)


#calculo imc pode ser feito de duas maneiras 
soma = int(peso / (altura * altura)) 
soma = peso / altura ** 2

print("Érka você tem ",altura, "altura")
print("Seu peso é ",peso)
print("A soma do seu IMC é ", soma)
print(type(...))

# Como podemos fomatar uma STR
# Quando usando o metodo f-string, podemos no final de cada elemento chamdo colocarmos a quantidade de casas decimais usando ("variavel":.2f)
print( f"{nome} tem {altura:.2f} de altura, seu peso é {peso} e seu IMC é {soma:.2f}")

# para colocar virgular em determinado número usamos (:,.2f)
valor = 105503
print(f"o valor é {valor:,.2f}")
#o valor é 105,503.00