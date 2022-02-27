import os
import csv
import smtplib
import ssl


navegador = ''


def cls():
    import os
    os.system('cls')


def criar_diretorio(caminho):
    if not os.path.exists(caminho):
        os.mkdir(caminho)


def salvar_csv(arquivo, modo, conteudo):
    arquivo_manipulado = open(arquivo, modo, encoding='utf8')
    escreva = csv.writer(arquivo_manipulado)
    escreva.writerow(conteudo)


def tratar_anexo(conteudo_anexo):
    conteudo_anexo = str(
        conteudo_anexo
    ).replace('[', '').replace('\\n', ' ')\
        .replace('"', '').replace(';', '')\
        .replace("', '", "'; '").replace(',', '')\
        .replace(';', ',').replace(']', '\r\n')
    return conteudo_anexo


def enviar_email_outlook(endereco_de, senha, endereco_para, mensagem):
    login = endereco_de.split('<')[1].replace('>', '')
    servidor = smtplib.SMTP('smtp.office365.com')
    servidor.connect("smtp.office365.com", 587)
    servidor.ehlo('hello')
    contexto = ssl.create_default_context()
    servidor.starttls(context=contexto)
    servidor.login(str(login), senha)
    cls()
    servidor.sendmail(endereco_de, endereco_para, mensagem)
    servidor.quit()

