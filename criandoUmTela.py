from PySimpleGUI import PySimpleGUI as sg
#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char="*")],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
],

#Janelas
janela = sg.Window('Tela de Login',layout)
#Ler evenos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        if valores ['usuario'] == 'Gildevan' and valores['senha'] == '123456':
            print(f'Bem vindo ao PYTHON👌😍')