import requests

#Variaveis
#url = 'https://pt.textbin.net/raw/qbqdmdtwur'
codigo = ''


def conexao_textbin(url):
    global codigo
    try:
        codigo = requests.get(url)
        codigo = codigo.status_code
    except Exception:
        pass
def requisicao(url):
    global codigo
    if codigo == 200:
        print('Verificando Atualização')
        codigo = requests.get(url).content
        codigo = codigo.decode('utf-8')
        configuracao_fun()
        if codigo[9:14] == texto[9:14]:
            print ('Sistema está atualizado!')
        else:
            print('Atualização Realizada!')
            atualizacao_fun()
    else:
        print('sem conexao')
def configuracao_fun():
    global texto
    arquivo = open('config.txt','r')
    texto= arquivo.read()
    arquivo.close()
def atualizacao_fun():
    global configuracao2
    global codigo2
    with open ('config.txt','w') as configuracao2:
        codigo2 = codigo.replace('\n','')
        configuracao2.write(codigo2)
def baixar_info(url):
    conexao_textbin(url)
    configuracao_fun()
    requisicao(url)
    arquivo = open('config.txt','r')
    texto= arquivo.read()
    arquivo.close()
    return texto
