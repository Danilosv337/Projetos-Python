import PySimpleGUI as sg
def tela_login():
    lista_emails = ["Hotmail","Gmail","Hostinger","Yahoo"]
    servidores_email = {
        "Hotmail":"outlook.office365.com",
        "Gmail":"imap.gmail.com",
        "Hostinger":"imap.hostinger.com",
        "Yahoo":"imap.mail.yahoo.com"
    }
    layout = [[sg.Text('Email ',background_color="#205CF5"),sg.Input(key="-Email-",size=(30,1))],
            [sg.Text('Senha',background_color="#205CF5"),sg.Input(key="-Senha-",password_char='*',size=(30,1))],
            [sg.Combo(lista_emails,key="-Servidor-",default_value="Hotmail")],
            [sg.Button("Login"),sg.Button("Sair")]]

    janela_login = sg.Window('Tela De Login',layout,background_color="#205CF5",titlebar_background_color="#205CF5",icon="process.ico")



    while True:
        evento, valor = janela_login.read()
        if evento == "Login":
            email = valor["-Email-"]
            senha= valor["-Senha-"]
            servidor = servidores_email[valor["-Servidor-"]]
            if "@" in email and senha != '':
                break
        if evento == sg.WIN_CLOSED or evento == 'Sair':
            email = None
            senha = None
            servidor = None
            return (None,None,None)

    janela_login.close()
    return email,senha,servidor





if __name__ == "__main__":
    tela_login()