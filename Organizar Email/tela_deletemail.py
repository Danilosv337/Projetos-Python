import PySimpleGUI as sg
from time import sleep
def tela_de_delete(meu_email,tamanho,emails_delete,emails_tela):
    layout = [[sg.Output(size=(80,20))],
            [sg.ProgressBar(tamanho, orientation='h', size=(20, 20), key='progressbar')],
            [sg.Button('Iniciar'),sg.Button("Sair")]]

    tela_delete = sg.Window("Deletar", layout,background_color="#205CF5",icon="process.ico")
    progress_bar = tela_delete['progressbar']

    while True:
        evento, valor = tela_delete.read()
        if evento == "Sair" or evento == sg.WIN_CLOSED:
            break
        if evento == "Iniciar":
            i = 0
            for i , email in enumerate(emails_delete):
                evento, valor = tela_delete.read(timeout=10)
                if evento == 'Sair'  or evento == sg.WIN_CLOSED:
                    break
                sleep(0.1)
                print(emails_tela[i])
                meu_email.delete(email)
                progress_bar.UpdateBar(i + 1)
                tela_delete.Refresh
            print("Finalizado")
            tela_delete.Refresh
    tela_delete.close()

