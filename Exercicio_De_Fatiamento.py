'''
Exercício
Peça ao usuári para digitar seu nome
peça ao usuário para digitar sua idade 
Se o nome e idade forem digitados
    Exiba:
        Seu nome é {}
        Seu nome invertido é{}
        Seu nome contém (ou não ) epaços
        Seu nome tem {} letrás
        A primeria letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade 
    Exiba:
        "Desculpa", você deixou campos vazios

'''

nome = input('Digite seu nome:\n')
idade = input('Digite sua Idade:\n')

try :
    nome and idade
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contem espçaos')

    print(f'Seu nome tem {len(nome)} letrás')
    print(f'A primeria letra do seu nome é {nome[0]}')
    print(f'A ultíma letra do seu nome é {nome[-1]}')
except:
    print(f'Desculpa, você deixou campos vazios')


