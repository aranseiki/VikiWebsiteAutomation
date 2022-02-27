from time import sleep
import selenium_utils as selenium
import python_functions_utils as custom
import csv

# INICIALIZA A AUTOMAÇÃO
url = "https://www.viki.com/"
selenium.iniciar_navegador(url)

# ENTRA NA PÁGINA DE LOGIN
seletor = 'li.hide-on-small:nth-child(4) > a:nth-child(1)'
selenium.encontrar_elemento(seletor)
selenium.clicar_elemento(seletor)

# INSERE O E-MAIL
seletor = "input[type="+"email"+"]"
selenium.encontrar_elemento(seletor)
selenium.escrever_no_elemento(seletor, input('digite seu e-mail: '))

# INSERE A SENHA
seletor = "input[type="+"password"+"]"
selenium.encontrar_elemento(seletor)
selenium.escrever_no_elemento(seletor, input('digite sua senha: '))

# LIMPA O TERMINAL POR SEGURANÇA
custom.cls()

# CLICA NO BOTÃO "LOGIN" PARA FAZER O LOGON
seletor = 'form > button'
selenium.encontrar_elemento(seletor)
selenium.clicar_elemento(seletor)

# CLICA NO LINK EXPLORAR NO MENU HORIZONTAL SUPERIOR
seletor = "a[href="+"'/explore'"+"]"
selenium.aguardar_elemento(seletor)
selenium.encontrar_elemento(seletor)
selenium.clicar_elemento(seletor)

# EXIBE TODOS OS FORMATOS DE SÉRIES
seletor = 'div#s2id_type > a > span.select2-arrow > b'
selenium.encontrar_elemento(seletor)
selenium.clicar_elemento(seletor)

# DEFINE O FORMATO DA SÉRIE COMO "TV"
seletor = "div#select2-drop > ul[role="+"listbox"+"] > li:nth-child(2)"
selenium.encontrar_elemento(seletor)
selenium.clicar_elemento(seletor)

current_country_selection = ''
while current_country_selection != 'Korea':
    # EXIBE TODOS OS OS PAÍSES DE ORIGEM
    seletor = 'div#s2id_country > a > span.select2-arrow > b'
    selenium.encontrar_elemento(seletor)
    selenium.clicar_elemento(seletor)

    # DEFINE O PÁIS DE ORIGEM COMO COREA
    seletor = "div#select2-drop > ul > li[role="+"presentation"+"] > ul.select2-result-sub > li[role="+"presentation"+"]:nth-child(2)  > div[class="+"select2-result-label"+"]"
    selenium.aguardar_elemento(seletor)
    selenium.encontrar_elemento(seletor)
    selenium.clicar_elemento(seletor)
    sleep(1)

    # VERIFICA SE A REGIÃO SELECIONADA CORRESPONDE COM O SOLICITADO
    seletor = "div#s2id_country > a[class="+"select2-choice"+"] > span[class="+"select2-chosen"+"]"
    current_country_selection = selenium.extrair_texto(seletor)

# EXIBE TODAS AS OPÇÕES DE ORDEM DAS SÉRIES
seletor = 'div.explore-sort-items > div > a > span:nth-child(2) > i'
selenium.aguardar_elemento(seletor)
selenium.encontrar_elemento(seletor)
selenium.clicar_elemento(seletor)

# DEFINE A ORDEM DE EXIBIÇÃO COMO "POPULAR-ALL TIME"
sleep(4)
seletor = 'div.explore-sort-items > div > ul > li:nth-child(1) > a'
selenium.aguardar_elemento(seletor)
selenium.encontrar_elemento(seletor)
selenium.clicar_elemento(seletor)

# INICIALIZA VALORES PARA A CONDIÇÃO DO WHILE
list_all_titles_movies_saved = []
link_next_page = True

# PARA CADA PÁGINA QUE CONTÉM A LISTA DE SÉRIES:
while link_next_page == True:
    try:
        # GARANTE QUE EXISTE A PRIMEIRA SÉRIE DA LISTA DISPONÍVEL NA PÁGINA
        seletor = 'div.row-inline > div.thumbnail:nth-child(1)'
        selenium.aguardar_elemento(seletor)
        # DEFINE wait_element COMO True PARA VALIDAÇÃO POSTERIOR
        wait_element = True
    except:
        # DEFINE wait_element COMO False PARA VALIDAÇÃO POSTERIOR
        wait_element = False
    
    # CASO wait_element SEJA FALSO
    if (wait_element == False):
        # ENCERRA A EXECUÇÃO DO LOOP
        break

    # INICIALIZA VALORES PARA A CONDIÇÃO DO WHILE
    contagem_atual = 1
    
    # AGUARDA O ELEMENTO GERAL DAS LISTAS FICAR DISPONÍVEL NA TELA
    seletor = 'div.row-inline > div.thumbnail'
    selenium.aguardar_elemento(seletor)

    # COLETA A QUANTIDADE DE SÉRIES QUE EXISTE VISÍVEL NA PÁGINA
    contagem_series = selenium.contar_elementos(seletor)

    # PARA CADA SÉRIE DA PÁGINA
    while contagem_atual <= contagem_series:
        # DEFINE O CAMINHO LÓGICO DA SÉRIE
        seletor = "div.row-inline > div.thumbnail:nth-child("+ str(contagem_atual) +") > div[class="+"'thumbnail-description dropdown-menu-wrapper'"+"] > div > a"

        # AGUARDA A SÉRIE FICAR VISÍVEL NA PÁGINA
        selenium.aguardar_elemento(seletor)

        # ENCONTRA A SÉRIE
        selenium.encontrar_elemento(seletor)

        # COLETA O NOME DA SÉRIE E SALVA NA LISTA
        list_all_titles_movies_saved.append(selenium.extrair_texto(seletor)+'\r\n')
        
        # CONDICIONAL PARA A LÓGICA DO LOOP
        contagem_atual = contagem_atual + 1

    try:
        # VERIFICA SE EXITE O LINK "NEXT"
        seletor = "div.pagination > a[rel="+"next"+"]"
        selenium.encontrar_elemento(seletor)
        # DEFINE link_next_page COMO True PARA VALIDAÇÃO POSTERIOR
        link_next_page = True
    except:
        # DEFINE link_next_page COMO False PARA VALIDAÇÃO POSTERIOR
        link_next_page = False

    # CASO EXISTA LINK "NEXT" NA PÁGINA
    if (link_next_page == True):
        # CLICA NO LINK "NEXT"
        selenium.clicar_elemento(seletor)

# DEFINE O CABEÇALHO DO ARQUIVO DE EXPORTAÇÃO .CSV
custom.salvar_csv('data.csv', 'w', ["Nome da série"])

# EXPORTA A LISTA DE SÉRIES PARA O ARQUIVO .CSV
custom.salvar_csv('data.csv', 'a', list_all_titles_movies_saved)
