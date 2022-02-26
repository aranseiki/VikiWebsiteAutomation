from selenium import webdriver
from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

navegador = Firefox()
url = "https://www.viki.com/"
navegador.get(url)

sleep(0.5)
loginPage = navegador.find_element(By.CSS_SELECTOR, 'li.hide-on-small:nth-child(4) > a:nth-child(1)')
loginPage.click()
sleep(0.5)
username = navegador.find_element(By.CSS_SELECTOR, 'input[type="email"]')
username.send_keys(input('digite seu e-mail: '))
sleep(0.5)
userpassword = navegador.find_element(By.CSS_SELECTOR, 'input[type="password"]')
userpassword.send_keys(input('digite sua senha: '))
sleep(0.5)
loginButton = navegador.find_element(By.TAG_NAME,'form > button')
loginButton.click()

"""
sleep(10)
explore_link = navegador.find_element(By.CSS_SELECTOR, 'span[data-tracking-id="header_explore"]')
explore_link.click()
"""

sleep(2)
link_all_shows = navegador.find_element(By.CSS_SELECTOR, 'a[href="/explore"]')
link_all_shows.click()

sleep(2)
select_box_formats = navegador.find_element(By.CSS_SELECTOR, 'div#s2id_type > a > span.select2-arrow > b')
select_box_formats.click()

sleep(2)
select_box_option_tv = navegador.find_element(By.CSS_SELECTOR, 'div#select2-drop > ul[role="listbox"] > li:nth-child(2)')
select_box_option_tv.click()

sleep(2)
select_box_countries = navegador.find_element(By.CSS_SELECTOR, 'div#s2id_country > a > span.select2-arrow > b')
select_box_countries.click()

sleep(2)
wait = WebDriverWait(navegador, 10)
select_box_option_korea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#select2-drop > ul > li[role="presentation"] > ul.select2-result-sub > li[role="presentation"]:nth-child(2)  > div[class="select2-result-label"]')))
select_box_option_korea.click()

sleep(2)
wait = WebDriverWait(navegador, 10)
link_sort_by = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.explore-sort-items > div > a > span:nth-child(2) > i')))
link_sort_by.click()

sleep(2)
wait = WebDriverWait(navegador, 10)
link_sort_by_option_all_time = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.explore-sort-items > div > ul > li:nth-child(1) > a')) and EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.explore-sort-items > div > ul > li:nth-child(1) > a')))
link_sort_by_option_all_time.click()

sleep(2)
link_next_page = navegador.find_element(By.CSS_SELECTOR, 'div.pagination > a[rel="next"]')


list_all_titles_movies_saved = []
number_page = 1
current_page = f'The current page is: ', number_page
print(current_page)

while link_next_page: 
    wait = WebDriverWait(navegador, 10)
    list_all_titles_movies = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.row-inline > div.thumbnail > div.thumbnail-description > div > a')))
    for i in list_all_titles_movies:
        list_all_titles_movies_saved.append(i.text+'\r\n')
    locator = (By.CSS_SELECTOR, 'div.pagination > a[rel="next"]')
    sleep(10)
    wait.until(EC.presence_of_element_located(locator) and EC.element_to_be_clickable(locator))
    link_next_page = navegador.find_element(By.CSS_SELECTOR, 'div.pagination > a[rel="next"]')
    link_next_page.click()
    sleep(6)
    number_page = number_page + 1
    current_page = f'The current page is: ', number_page
    print(current_page)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.pagination > a[rel="next"]')), 'Elemento não encontrado! ')
    link_next_page = navegador.find_element(By.CSS_SELECTOR, 'div.pagination > a[rel="next"]')
    

print(list_all_titles_movies_saved)
with open('data.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(list_all_titles_movies_saved)
