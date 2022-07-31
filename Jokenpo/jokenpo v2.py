import random


cred='\033[31m'
cblue='\033[34m'
cgreen='\033[32m'
negrito='\033[1m'
sublinhar='\033[4m'
limpar='\033[m'

jokenpo=['PEDRA','PAPEL','TESOURA']

while True:

    escolha = input(f'{cred}Oque voce escolhe? pedra,papel ou tesoura? ')
    def escolha_pedra():
        escolha = 'PEDRA'
        pc=random.choice(jokenpo)
        if escolha == pc:
            print('\n{}Eita, Empatou!{}'.format(cgreen,limpar))
        if escolha == 'PEDRA' and pc == 'TESOURA':
            print('\n{}Voce Ganhou!{}'.format(cgreen,limpar))
        elif escolha == 'PEDRA' and pc == 'PAPEL':
            print('\n{}lamento voce perdeu{}'.format(cred,limpar))
    def escolha_papel():
        escolha='PAPEL'
        pc=random.choice(jokenpo)
        if escolha == pc:
            print('\n{}Eita, Empatou!{}'.format(cgreen,limpar))
        if escolha ==  'PAPEL' and pc == 'PEDRA':
            print('\n{}Parabéns Você Ganhou!{}'.format(cgreen,limpar))
        elif escolha == 'PAPEL' and pc == 'TESOURA':
            print ('\n{}Você perdeu!{}'.format(cred,limpar))
    def escolha_tesoura():
        escolha='TESOURA'
        pc=random.choice(jokenpo)
        if escolha == pc:
            print('\n{}Eita, Empatou!{}'.format(cgreen,limpar))
        if escolha == 'TESOURA' and pc == 'PAPEL':
            print('\n{}Voce Ganhou!{}'.format(cgreen,limpar))
        elif escolha == 'TESOURA' and pc == 'PEDRA':
            print('\n{}Lamento Voce perdeu!{}'.format(cred,limpar)) 
    if escolha == ('pedra'):
        escolha_pedra()
    elif escolha == ('papel'):
        escolha_papel()
    elif escolha == ('tesoura'):
        escolha_tesoura()
