from time import sleep
import selenium_utils as selenium
import python_functions_utils as custom
import csv

# OPEN THE BROWSE WITH A URL
url = "https://www.viki.com/"
selenium.start_browser(url)

# ACCESS THE LOGIN PAGE
selector = 'li.hide-on-small:nth-child(4) > a:nth-child(1)'
selenium.find_element(selector)
selenium.click_element(selector)

# INSERT THE E-MAIL
selector = "input[type="+"email"+"]"
selenium.find_element(selector)
selenium.write_in_element(selector, input('Type your e-mail: '))

# INSERT THE PASSWORD
selector = "input[type="+"password"+"]"
selenium.find_element(selector)
selenium.write_in_element(selector, input('Type your password: '))

# CLEAR THE TERMINAL FOR SECURITY
custom.cls()

# CLICK ON THE "LOGIN" BUTTON
selector = 'form > button'
selenium.find_element(selector)
selenium.click_element(selector)

# CLICK IN "EXPLORER" LINK ON TOP OF MENU HORIZONTAL
selector = "a[href="+"'/explore'"+"]"
selenium.wait_element(selector)
selenium.find_element(selector)
selenium.click_element(selector)

# SHOW ALL TV SERIES FORMATS
selector = 'div#s2id_type > a > span.select2-arrow > b'
selenium.find_element(selector)
selenium.click_element(selector)

# DEFINE "TV" OPTION AS SERIE FORMAT SELECTIONED
selector = "div#select2-drop > ul[role="+"listbox"+"] > li:nth-child(2)"
selenium.find_element(selector)
selenium.click_element(selector)

# INITIALIZE THE VARIABLES FOR LOGIC
current_country_selection = ''
tentatives = 1
while tentatives <= 5:
    # SHOW ALL ORIGIN'S COUNTRY OPTIONS
    selector = 'div#s2id_country > a > span.select2-arrow > b'
    selenium.find_element(selector)
    selenium.click_element(selector)

    # DEFINE THE COUNTRY OPTION AS KOREA
    selector = "div#select2-drop > ul > li[role="+"presentation"+"] > ul.select2-result-sub > li[role="+"presentation"+"]:nth-child(2)  > div[class="+"select2-result-label"+"]"
    selenium.wait_element(selector)
    selenium.find_element(selector)
    selenium.click_element(selector)
    sleep(1)

    # STORE THE SELECTIONED REGION
    selector = "div#s2id_country > a[class="+"select2-choice"+"] > span[class="+"select2-chosen"+"]"
    current_country_selection = selenium.extract_text(selector)
    
    # CONDITION FOR THE LOOP'S LOGIC
    tentatives = tentatives + 1
    
    # IF THE SELECTIONED REGION MATCH WITH THE OPTION REQUESTED
    if current_country_selection == 'Korea':
        # EXIT OF THE LOOP
        break
    # IF THE SELECTIONED REGION NOT MATCH WITH THE OPTION REQUESTED
    else:
        # WAIT 1 SECOUND
        sleep(1)

current_country_selection = ''
tentatives = 1
while tentatives <= 5:
    # SHOW ALL SERIES ORDER OPTIONS
    selector = 'div.explore-sort-items > div > a > span:nth-child(2) > i'
    selenium.wait_element(selector)
    selenium.find_element(selector)
    selenium.click_element(selector)
    
    # DEFINE THE SELECTIONED SERIES ORDER AS "POPULAR-ALL TIME"
    selector = 'div.explore-sort-items > div > ul > li:nth-child(1) > a'
    selenium.wait_element(selector)
    selenium.find_element(selector)
    selenium.click_element(selector)
    sleep(2)

    # STORE THE SELECTIONED SERIES ORDER
    selector = "div.explore-sort-items > div > a > span:nth-child(2)"
    current_order_selection = selenium.extract_text(selector)
    
    # CONDITION FOR THE LOOP'S LOGIC
    tentatives = tentatives + 1
    
    # IF THE SELECTIONED SERIES ORDER MATCH WITH THE OPTION REQUESTED
    if current_order_selection.__contains__('Popular - All Time'):
        # EXIT OF THE LOOP
        break
    # IF THE SELECTIONED SERIES ORDER NOT MATCH WITH THE OPTION REQUESTED
    else:
        # WAIT 1 SECOUND
        sleep(1)

# INITIALIZE VALUES FOR THE WHILE-LOOP'S CONDITIONS
list_all_titles_movies_saved = []
link_next_page = True

# FOR EACH PAGE THAT CONTAINS THE SERIES LIST
while link_next_page == True:
    try:
        # ASSERT THAT EXISTS THE FIRST SERIE IN THE AVALIABLE ON PAGE
        selector = 'div.row-inline > div.thumbnail:nth-child(1)'
        selenium.wait_element(selector)
        # DEFINE wait_element AS True FOR POSTERIOR AVALIATION
        wait_element = True
    except:
        # DEFINE wait_element AS False FOR POSTERIOR AVALIATION
        wait_element = False
    
    # IF wait_element BE False
    if (wait_element == False):
        # EXIT THE LOOP EXECUTION
        break

    # INITIALIZE VALUES FOR THE WHILE-LOOP'S CONDITION
    counter_current = 1
    
    # WAIT THE GENERAL ELEMENT OF ELEMENT'S LIST TO BE AVALIABLE IN THE SCREEN
    selector = 'div.row-inline > div.thumbnail'
    selenium.wait_element(selector)

    # STORE THE LENGTH OF SERIES AVALIABLES IN THE PAGE
    counter_series = selenium.counter_elements(selector)

    # FOR EACH SERIE IN THE PAGE
    while counter_current <= counter_series:
        # DEFINE THE LOGIC LOCAL OF THE SERIE
        selector = "div.row-inline > div.thumbnail:nth-child("+ str(counter_current) +") > div[class="+"'thumbnail-description dropdown-menu-wrapper'"+"] > div > a"

        # WAIT THE CURRENT SERIE BE AVALIABLE IN THE PAGE
        selenium.wait_element(selector)

        # FINDS CURRENT SERIE
        selenium.find_element(selector)

        # STORE THE NAME OF SERIE AND SAVE IT IN THE LIST
        list_all_titles_movies_saved.append(selenium.extract_text(selector))
        
        # CONDITION FOR THE LOOP'S LOGIC
        counter_current = counter_current + 1

    try:
        # FIND THE "NEXT" LINK IN THE BOTTOM PAGE
        selector = "div.pagination > a[rel="+"next"+"]"
        selenium.find_element(selector)
        # DEFINE link_next_page AS True FOR POSTERIOR AVALIATION
        link_next_page = True
    except:
        # DEFINE link_next_page AS False FOR POSTERIOR AVALIATION
        link_next_page = False

    # IF EXISTS "NEXT" LINK IN THE PAGE
    if (link_next_page == True):
        # CLICK IN THE "NEXT" LINK
        selenium.click_element(selector)

# DEFINE THE HEADER OF FILE'S EXPORT .CSV
custom.save_csv('data.csv', 'w', ["Nome da série"])

# EXPORTS THE SERIES LIST FOR THE FILE .CSV
custom.save_csv('data.csv', 'a', custom.serie_list_handling(list_all_titles_movies_saved))

# CLOSE THE BROWSER
selenium.stop_browser()
