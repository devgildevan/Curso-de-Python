'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
valor_do_usuario = input('Vou dobrar o valor do seu número:\n')

try:
    numero_float = float(valor_do_usuario)
    print('Float:', numero_float)
    print(f'O dobro de {valor_do_usuario} é {numero_float * 2:.1f} ')

except:
    print('O VALOR DIGITADO NÃO É NÚMERO')


# isdigit é um metodo que usamos para identificar se o usuário de fato escreveu  um input de valor númerico
# if valor_do_usuario.isdigit():
#     numero_float = float(valor_do_usuario)
#     print(f'O dobro de {valor_do_usuario} é {numero_float * 2:.1f} ')

# else:
#     print('O VALOR DIGITADO NÃO É NÚMERO')