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
loginPage = navegador.find_element_by_partial_link_text("Log in")
loginPage.click()
sleep(0.5)
username = navegador.find_element_by_id("login_id")
username.send_keys("techall@hotmail.com.br")
sleep(0.5)
userpassword = navegador.find_element_by_id("password")
userpassword.send_keys("Ainouta@773912")
sleep(0.5)
loginButton = navegador.find_element_by_css_selector('input[value="Log in"]')
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
openDrama = navegador.find_element_by_css_selector('[href="/tv/902c-dream-high"]')
openDrama.click()

sleep(2)
listaAllEpisodios = navegador.find_element_by_css_selector('[data-block-track="videoEpisodesSeeAll"]')
listaAllEpisodios.click()

"""
paginaContinueAssistindo = navegador.find_element_by_css_selector('[class="sc-1b82lv6-2 hesMYj"]')
paginaContinueAssistindo.click()
"""