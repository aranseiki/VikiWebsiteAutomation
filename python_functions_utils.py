import os
import csv
import smtplib
import ssl


navegador = ''


def cls():
    import os
    os.system('cls')


def create_directory(caminho):
    if not os.path.exists(caminho):
        os.mkdir(caminho)


def save_csv(arquivo, modo, conteudo):
    arquivo_manipulado = open(arquivo, modo, encoding='utf8')
    escreva = csv.writer(arquivo_manipulado)
    escreva.writerow(conteudo)


def handling_attachment(conteudo_anexo):
    conteudo_anexo = str(
        conteudo_anexo
    ).replace('[', '').replace('\\n', ' ')\
        .replace('"', '').replace(';', '')\
        .replace("', '", "'; '").replace(',', '')\
        .replace(';', ',').replace(']', '\r\n')
    return conteudo_anexo


def send_email_outlook(endereco_de, senha, endereco_para, mensagem):
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


def serie_list_handling(list_param):
    return str(list_param)\
        .replace("', \'", ', ')\
        .replace('\\r\\n,', '\r\n')\
        .replace('\r', "', '")\
        .replace('\\r', "', '")\
        .replace('\n', "', '")\
        .replace('\\n', "', '")\
        .replace("']", '')\
        .replace('"]', "")\
        .replace('"', "'")\
        .replace('"', "")\
        .replace('""', "")\
        .replace("''", "")\
        .replace("', , '", "', '")\
        .replace("' ", "'")\
        .replace(", ,", "")\
        .replace("' ,", "',")\
        .replace("', '", ";")\
        .split('\r\n')
