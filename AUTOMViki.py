from time import sleep
import selenium_utils as selenium
import python_functions_utils as custom
import csv

# INICIALIZA A AUTOMAÇÃO
url = "https://www.viki.com/"
selenium.start_browser(url)
a
# ENTRA NA PÁGINA DE LOGIN
selector = 'li.hide-on-small:nth-child(4) > a:nth-child(1)'
selenium.find_element(selector)
selenium.click_element(selector)

# INSERE O E-MAIL
selector = "input[type="+"email"+"]"
selenium.find_element(selector)
selenium.write_in_element(selector, input('Type your e-mail: '))

# INSERE A SENHA
selector = "input[type="+"password"+"]"
selenium.find_element(selector)
selenium.write_in_element(selector, input('Type your password: '))

# LIMPA O TERMINAL POR SEGURANÇA
custom.cls()

# CLICA NO BOTÃO "LOGIN" PARA FAZER O LOGON
selector = 'form > button'
selenium.find_element(selector)
selenium.click_element(selector)

# CLICA NO LINK EXPLORAR NO MENU HORIZONTAL SUPERIOR
selector = "a[href="+"'/explore'"+"]"
selenium.wait_element(selector)
selenium.find_element(selector)
selenium.click_element(selector)

# EXIBE TODOS OS FORMATOS DE SÉRIES
selector = 'div#s2id_type > a > span.select2-arrow > b'
selenium.find_element(selector)
selenium.click_element(selector)

# DEFINE O FORMATO DA SÉRIE COMO "TV"
selector = "div#select2-drop > ul[role="+"listbox"+"] > li:nth-child(2)"
selenium.find_element(selector)
selenium.click_element(selector)

current_country_selection = ''
tentatives = 1
while tentatives <= 5:
    # EXIBE TODOS OS OS PAÍSES DE ORIGEM
    selector = 'div#s2id_country > a > span.select2-arrow > b'
    selenium.find_element(selector)
    selenium.click_element(selector)

    # DEFINE O PÁIS DE ORIGEM COMO COREA
    selector = "div#select2-drop > ul > li[role="+"presentation"+"] > ul.select2-result-sub > li[role="+"presentation"+"]:nth-child(2)  > div[class="+"select2-result-label"+"]"
    selenium.wait_element(selector)
    selenium.find_element(selector)
    selenium.click_element(selector)
    sleep(1)

    # COLETA A REGIÃO SELECIONADA
    selector = "div#s2id_country > a[class="+"select2-choice"+"] > span[class="+"select2-chosen"+"]"
    current_country_selection = selenium.extract_text(selector)
    tentatives = tentatives + 1
    
    # SE A REGIÃO SELECIONADA CORRESPONDER COM O SOLICITADO
    if current_country_selection == 'Korea':
        # SAI DO LOOP
        break
    # SE A REGIÃO SELECIONADA NÃO CORRESPONDER COM O SOLICITADO
    else:
        # AGUARDA 1 SEGUNDO
        sleep(1)

current_country_selection = ''
tentatives = 1
while tentatives <= 5:
    # EXIBE TODAS AS OPÇÕES DE ORDEM DAS SÉRIES
    selector = 'div.explore-sort-items > div > a > span:nth-child(2) > i'
    selenium.wait_element(selector)
    selenium.find_element(selector)
    selenium.click_element(selector)
    
    # DEFINE A ORDEM DE EXIBIÇÃO COMO "POPULAR-ALL TIME"
    selector = 'div.explore-sort-items > div > ul > li:nth-child(1) > a'
    selenium.wait_element(selector)
    selenium.find_element(selector)
    selenium.click_element(selector)
    sleep(2)

    # COLETA A ORDEM DE EXIBIÇÃO SELECIONADA
    selector = "div.explore-sort-items > div > a > span:nth-child(2)"
    current_order_selection = selenium.extract_text(selector)
    
    # SE A ORDEM DE EXIBIÇÃO SELECIONADA CORRESPONDER COM O SOLICITADO
    if current_order_selection.__contains__('Popular - All Time'):
        # SAI DO LOOP
        break
    # SE A ORDEM DE EXIBIÇÃO SELECIONADA NÃO CORRESPONDER COM O SOLICITADO
    else:
        # AGUARDA 1 SEGUNDO
        sleep(1)

# INICIALIZA VALORES PARA A CONDIÇÃO DO WHILE
list_all_titles_movies_saved = []
link_next_page = True

# PARA CADA PÁGINA QUE CONTÉM A LISTA DE SÉRIES:
while link_next_page == True:
    try:
        # GARANTE QUE EXISTE A PRIMEIRA SÉRIE DA LISTA DISPONÍVEL NA PÁGINA
        selector = 'div.row-inline > div.thumbnail:nth-child(1)'
        selenium.wait_element(selector)
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
    counter_current = 1
    
    # AGUARDA O ELEMENTO GERAL DAS LISTAS FICAR DISPONÍVEL NA TELA
    selector = 'div.row-inline > div.thumbnail'
    selenium.wait_element(selector)

    # COLETA A QUANTIDADE DE SÉRIES QUE EXISTE VISÍVEL NA PÁGINA
    counter_series = selenium.counter_elements(selector)

    # PARA CADA SÉRIE DA PÁGINA
    while counter_current <= counter_series:
        # DEFINE O CAMINHO LÓGICO DA SÉRIE
        selector = "div.row-inline > div.thumbnail:nth-child("+ str(counter_current) +") > div[class="+"'thumbnail-description dropdown-menu-wrapper'"+"] > div > a"

        # AGUARDA A SÉRIE FICAR VISÍVEL NA PÁGINA
        selenium.wait_element(selector)

        # ENCONTRA A SÉRIE
        selenium.find_element(selector)

        # COLETA O NOME DA SÉRIE E SALVA NA LISTA
        list_all_titles_movies_saved.append(selenium.extract_text(selector))
        
        # CONDICIONAL PARA A LÓGICA DO LOOP
        counter_current = counter_current + 1

    try:
        # VERIFICA SE EXITE O LINK "NEXT"
        selector = "div.pagination > a[rel="+"next"+"]"
        selenium.find_element(selector)
        # DEFINE link_next_page COMO True PARA VALIDAÇÃO POSTERIOR
        link_next_page = True
    except:
        # DEFINE link_next_page COMO False PARA VALIDAÇÃO POSTERIOR
        link_next_page = False

    # CASO EXISTA LINK "NEXT" NA PÁGINA
    if (link_next_page == True):
        # CLICA NO LINK "NEXT"
        selenium.click_element(selector)

# DEFINE O CABEÇALHO DO ARQUIVO DE EXPORTAÇÃO .CSV
custom.save_csv('data.csv', 'w', ["Nome da série"])

# EXPORTA A LISTA DE SÉRIES PARA O ARQUIVO .CSV
custom.save_csv('data.csv', 'a', custom.serie_list_handling(list_all_titles_movies_saved))

selenium.stop_browser()
