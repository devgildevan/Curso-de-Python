primeiro_valor = input("Digite um valor:\n")
segundo_valor = input("Digite outro valor:\n")

if primeiro_valor > segundo_valor:
    print(f"O {primeiro_valor=} é maior que o {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"O {segundo_valor=} é maior que o {primeiro_valor=}")
elif primeiro_valor == segundo_valor:
    print("Os valores são identicos")
else:
    print("FIM!")

