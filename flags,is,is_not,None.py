'''
Flag (Bandeira) - Marcar um local
None - Não valor
is / is not = é ou não é (tipo,valor, identidade)
id = Identidade
'''

condicao = False
passou_no_If = None

if condicao:
    passou_no_If : True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_If is None:
    print('Não passou no IF')
else:
    print('Passou no IF')