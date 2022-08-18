import PySimpleGUI as sg
from sistema import organizar


layout = [  [sg.Text("Selecione Uma Pasta",key="caminho",background_color='#0476D9')],
            [sg.Button('Selecionar'),sg.Button('Organizar'),sg.Button('Sair')]]


interface = sg.Window('', layout,background_color='#0476D9', button_color = "#0460D9",icon="icone_mp3.ico",size=(220,70))

while True:
    event, values = interface.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == "Selecionar":
        pasta = sg.popup_get_folder("Selecione a Pasta!",background_color='#0476D9', button_color = "#0460D9",icon="icone_mp3.ico")
        interface["caminho"].update(pasta)
    if event == 'Organizar':
        organizar(pasta)
interface.close()