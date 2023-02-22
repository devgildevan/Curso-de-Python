
'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
entrada =input('Digite um número inteiro: \n')


try:
    entrada.isdigit()
    # numero = int(entrada)
    if int(entrada) % 2 == 0:
        nome = 'PAR'
    else:
        nome = 'ÌMPA'
    
    print(f'O número digitado {int(entrada)} é {nome}')
except: 
    print('Numero não é inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
usuario = input('Que horas já é ?:\n')

try:
    horas = int(usuario)
    if horas >= 0 and horas <= 11:
        print('Bom dia')
    elif horas >= 12 and horas <= 17:
        print('Boa Tarde')
    elif horas >= 18 and horas <= 23:
        print('Boa noite')
  

except:
    print('Digite uma hora valida')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = input('Digite seu primeiro nome: \n')

try:
    # letras = len(nome)
    if len(nome) <= 4 :
        print('Seu nome é curto')
    elif len(nome) >= 5 :
        print(f'Seu nom é normal {nome} e tem ({len(nome)})letras')
except:
    print('Né um nome')