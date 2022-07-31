import random
from tkinter import *

'''Código Não Pronto'''

#variaveis
vidas=100
pc=''
jokenpo=['PEDRA','PAPEL','TESOURA']
errado=''
pontos=''
escolha=''

#cores
cred='\033[31m'
cblue='\033[34m'
cgreen='\033[32m'
negrito='\033[1m'
sublinhar='\033[4m'
limpar='\033[m'

#Tkinter
app = Tk()
app.title('Jokenpô')
app.geometry('500x300')
texto_funcao = Label(app, text='Jokenpo')
texto_funcao.grid(column=0, row=0)



def Pedra():
    escolha='PEDRA'
    pc=random.choice(jokenpo)
    if escolha == pc:
        print('\n{}Eita, Empatou!{}'.format(cgreen,limpar))
    if escolha == 'PEDRA' and pc == 'TESOURA':
        print('\n{}Voce Ganhou!{}'.format(cgreen,limpar))
    elif escolha == 'PEDRA' and pc == 'PAPEL':
        print('\n{}lamento voce perdeu{}'.format(cred,limpar))
def Tesoura():
    escolha='TESOURA'
    pc=random.choice(jokenpo)
    if escolha == pc:
        print('\n{}Eita, Empatou!{}'.format(cgreen,limpar))
    if escolha == 'TESOURA' and pc == 'PAPEL':
        print('\n{}Voce Ganhou!{}'.format(cgreen,limpar))
    elif escolha == 'TESOURA' and pc == 'PEDRA':
        print('\n{}Lamento Voce perdeu!{}'.format(cred,limpar)) 
def Papel():
    escolha='PAPEL'
    pc=random.choice(jokenpo)
    if escolha == pc:
        print('\n{}Eita, Empatou!{}'.format(cgreen,limpar))
    if escolha ==  'PAPEL' and pc == 'PEDRA':
        print('\n{}Parabéns Você Ganhou!{}'.format(cgreen,limpar))
    elif escolha == 'PAPEL' and pc == 'TESOURA':
        print ('\n{}Você perdeu!{}'.format(cred,limpar))
        
btn1= Button(app,text='PEDRA',command=Pedra)
btn1.grid(column=0,row=1)
btn2= Button(app,text='PAPEL',command=Tesoura)
btn2.grid(column=1,row=1)
btn3= Button(app,text='TESOURA',command=Papel)
btn3.grid(column=2,row=1)

app.mainloop()