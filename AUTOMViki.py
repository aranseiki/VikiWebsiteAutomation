from platform import platform
from selenium import webdriver
from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import ( presence_of_element_located)

navegador = Firefox()
url = "https://www.viki.com/"
navegador.get(url)

sleep(0.5)
loginPage = navegador.find_element_by_css_selector('li>a[href="/sign_in"]')
loginPage.click()
sleep(0.5)
username = navegador.find_element_by_css_selector('input[type="email"]')
username.send_keys("techall@hotmail.com.br")
sleep(0.5)
userpassword = navegador.find_element_by_css_selector('input[type="password"]')
userpassword.send_keys("Ainouta@773912")
sleep(0.5)
loginButton = navegador.find_element_by_tag_name('form > button')
loginButton.click()

sleep(10)
enterMenuPerfil = navegador.find_element_by_css_selector('[class="circle va-top"]')
enterMenuPerfil.click()
sleep(0.5)
enterPerfil = navegador.find_element_by_css_selector('[href="/users/techall_399"]')
enterPerfil.click()
sleep(5)
paginaSeguindo = navegador.find_element_by_css_selector('[class="section block-display"]')
paginaSeguindo.click()

sleep(5)
openDrama = navegador.find_element_by_css_selector('[href="/tv/35883c-legend-of-yun-xi"]')
openDrama.click()

sleep(2)
listaAllEpisodios = navegador.find_element_by_css_selector('[class="sc-kEYyzF cyOvgX btn sc-1ae9vu4-0 hSXBky"]')
listaAllEpisodios.click()

def esperar_elemento(webdriver):
    elemento_esperar = webdriver.find_element_by_css_selector('[class="vjs-big-play-button"]')
    return bool (elemento_esperar)

esperarAte = WebDriverWait(navegador, 10)
esperarAte.until (esperar_elemento, 'Tente novamente mais tarde...')

playNoVideo = navegador.find_element_by_css_selector('[class="vjs-big-play-button"]')
playNoVideo.click()

def tela_cheia(botao_de_tela_cheia):
    elemento_tela_cheia = botao_de_tela_cheia.find_element_by_css_selector('[class="vjs-big-play-button"]')
    return bool (elemento_tela_cheia)

fullScreen = WebDriverWait(navegador, 5, poll_frequency=0.1)
fullScreen.until (tela_cheia, 'Tente novamente mais tarde...')

fullScreen = navegador.find_element_by_css_selector('[class="vjs-big-play-button"]')
navegador.fullscreen_window()