from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


navegador = ''


def iniciar_navegador(url):
    global navegador
    navegador = Firefox()
    navegador.get(url)
    aguardar_pagina_carregar()


def aguardar_pagina_carregar():
    estado_pronto = False
    while estado_pronto == False:
        estado = navegador.execute_script(
            'return window.document.readyState'
        )
        if estado != 'complete':
            sleep(1)
        else:
            estado_pronto = True


def voltar_pagina():
    navegador.back()
    aguardar_pagina_carregar()


def centralizar_elemento(seletor):
    navegador.execute_script(
        'document.querySelector("' + seletor
        + '").scrollIntoView({block: "center"})'
    )


def aguardar_elemento(seletor, tempo=30):
    try:
        wait = WebDriverWait(navegador, tempo)
        sleep(0.5)
        wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, seletor)
            ))
        centralizar_elemento(seletor)
        aguardar_pagina_carregar()
    except:
        ...


def encontrar_elemento(seletor):
    navegador.find_element(By.CSS_SELECTOR, seletor)
    centralizar_elemento(seletor)


def encontrar_varios_elementos(seletor):
    navegador.find_elements(By.CSS_SELECTOR, seletor)
    centralizar_elemento(seletor)


def contar_elementos(seletor):
    elementos = navegador.find_elements(By.CSS_SELECTOR, seletor)
    centralizar_elemento(seletor)
    return elementos.__len__()


def extrair_texto(seletor):
    elemento = navegador.find_element(By.CSS_SELECTOR, seletor)
    texto_elemento = elemento.text
    centralizar_elemento(seletor)
    return texto_elemento


def clicar_elemento(seletor):
    try:
        centralizar_elemento(seletor)
        elemento = navegador.find_element(By.CSS_SELECTOR, seletor)
        elemento.click()
        aguardar_pagina_carregar()
    except:
        ...


def escrever_no_elemento(seletor, texto):
    centralizar_elemento(seletor)
    elemento = navegador.find_element(By.CSS_SELECTOR, seletor)
    elemento.send_keys(texto)
    aguardar_pagina_carregar()


def clique_mouse(webelemento):
    action = ActionChains(navegador)
    action.double_click(webelemento).perform()


def encerrar_navegador():
    navegador.close()
