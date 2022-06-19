import random
from time import sleep
from os import system
from emoji import emojize
from tkinter import *

'''Código Não Pronto'''

#variaveis
vidas=1
pc=''
jokenpo=['PEDRA','PAPEL','TESOURA']
errado=''
emojivida=':red_heart:'
pontos=''
Pedra=''

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
texto_funcao = Label(app, text='valor1')
texto_funcao.grid(column=0, row=0, padx=10,pady=10)
btn1= Button(app,text='PEDRA',command=Pedra)
btn1.grid(column=0,row=1)
btn2= Button(app,text='PAPEL',command=Pedra)
btn2.grid(column=1,row=1)
btn3= Button(app,text='TESOURA',command=Pedra)
btn3.grid(column=2,row=1)


def Pedra():
    print('teste')
while vidas>0:
    system('cls')
    print(emojize('{}{}{}Jokenpô Feito Por Danilo Santos {}{}  {} Vidas Restantes {}'.format(negrito,cblue,sublinhar,cred,emojivida,vidas,limpar)))
    escolha=input('{}{}Você Escolhe Pedra, Papel Ou Tesoura?{} \n '.format(negrito,cblue,limpar))
    pc=random.choice(jokenpo)
    escolha=escolha.upper()
    pc=pc.upper()
    if escolha == 'SAIR':
        #break
        vidas=0
    if escolha == pc:
        print('\n{}Eita, Empatou!{}'.format(cgreen,limpar))
    #pedra
    if escolha == 'PEDRA' and pc == 'TESOURA':
        print('\n{}Voce Ganhou!{}'.format(cgreen,limpar))
        pontos += +1
    elif escolha == 'PEDRA' and pc == 'PAPEL':
        print('\n{}lamento voce perdeu{}'.format(cred,limpar))
        vidas += -1 
    #tesoura
    if escolha == 'TESOURA' and pc == 'PAPEL':
        print('\n{}Voce Ganhou!{}'.format(cgreen,limpar))
        pontos += +1
    elif escolha == 'TESOURA' and pc == 'PEDRA':
        print('\n{}Lamento Voce perdeu!{}'.format(cred,limpar))
        vidas += -1
    #papel
    if escolha ==  'PAPEL' and pc == 'PEDRA':
        print('\n{}Parabéns Você Ganhou!{}'.format(cgreen,limpar))
        pontos += +1
    elif escolha == 'PAPEL' and pc == 'TESOURA':
        print ('\n{}Você perdeu!{}'.format(cred,limpar))
        vidas += -1
    if escolha in jokenpo:
        print('\n{}O computador escolheu {}{}'.format(cblue,pc,limpar))
    else:
        print('\n{}{}Voce digitou algo errado!{}'.format(negrito,cred,limpar))
    sleep(2)
    if vidas == 0:
        system('cls')
        print('{}{}Voce Marcou {} Pontos{}'.format(negrito,cgreen,pontos,limpar))
        sleep (5)


app.mainloop()