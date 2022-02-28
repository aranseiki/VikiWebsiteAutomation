from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


browser = ''


def start_browser(url):
    global browser
    browser = Firefox()
    browser.get(url)
    wait_page_loaded()


def wait_page_loaded():
    done_state = False
    while done_state == False:
        state = browser.execute_script(
            'return window.document.readyState'
        )
        if state != 'complete':
            sleep(1)
        else:
            done_state = True


def back_page():
    browser.back()
    wait_page_loaded()


def center_element(selector):
    browser.execute_script(
        'document.querySelector("' + selector
        + '").scrollIntoView({block: "center"})'
    )


def wait_element(selector, time=30):
    try:
        wait = WebDriverWait(browser, time)
        sleep(0.5)
        wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, selector)
            ))
        center_element(selector)
        wait_page_loaded()
    except:
        ...


def find_very_elements(selector):
    browser.find_elements(By.CSS_SELECTOR, selector)
    center_element(selector)


def find_element(selector):
    browser.find_elements(By.CSS_SELECTOR, selector)
    center_element(selector)


def counter_elements(selector):
    elements = browser.find_elements(By.CSS_SELECTOR, selector)
    center_element(selector)
    return elements.__len__()


def extract_text(selector):
    element = browser.find_element(By.CSS_SELECTOR, selector)
    text_element = element.text
    center_element(selector)
    return text_element


def click_element(selector):
    try:
        center_element(selector)
        element = browser.find_element(By.CSS_SELECTOR, selector)
        element.click()
        wait_page_loaded()
    except:
        ...


def write_in_element(selector, text):
    center_element(selector)
    element = browser.find_element(By.CSS_SELECTOR, selector)
    element.send_keys(text)
    wait_page_loaded()


def mouse_click(webelement):
    action = ActionChains(browser)
    action.double_click(webelement).perform()


def stop_browser():
    browser.close()
