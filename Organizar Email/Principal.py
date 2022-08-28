from imap_tools import MailBox, AND
from tela_login import tela_login
from tela_deletemail import tela_de_delete
import PySimpleGUI as sg





def logar(email,senha,servidor):

    meu_email = MailBox(servidor).login(email,senha)
    return meu_email


def lista_de_emails(meu_email):
    emails_mover = []
    lista_emails = meu_email.fetch(AND(all=True))
    return lista_emails



if __name__ == "__main__":
    while True:
        email, senha, servidor = tela_login()
        if email == None:
            break
        try:
            meu_email = logar(email,senha,servidor)
            break
        except:
            sg.SystemTray.notify("Error","Falha Ao Realizar Login!")
    try:
        lista_emails = lista_de_emails(meu_email)
        emails_delete = []
        emails_tela = []


        for email in lista_emails:
            emails_delete.append(email.uid)
            emails_tela.append(email.subject)
            sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', time_between_frames=100)
        sg.PopupAnimated(None)
        tamanho = len(emails_delete)
        tela_de_delete(meu_email,tamanho,emails_delete,emails_tela)
    except:
        pass
