from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


browser = ''


def start_browser(url):
    """
    Definition
    ----------
    Starts the Firefox browser and open it with an URL.
    Require to inform URL parameter.
    ----------

    Parameters
    ----------
        url : str
            Link URL of a valid webpage
    ----------

    Output
    ----------
    None

    """
    global browser
    browser = Firefox()
    browser.get(url)
    wait_page_loaded()


def wait_page_loaded():
    """
    Definition
    ----------
    Waits the current webpage in context be totally fulled.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
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
    """
    Definition
    ----------
    Back the navigation for earlierly webpage accessed.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    browser.back()
    wait_page_loaded()


def center_element(selector):
    """
    Definition
    ----------
    centralizes a webelement to center of screen.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    browser.execute_script(
        'document.querySelector("' + selector
        + '").scrollIntoView({block: "center"})'
    )


def wait_element(selector, time=30):
    """
    Definition
    ----------
    Waits a element in the current webpage in context be \
        totally visible.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]
    time : int
        Time, in seconds, that will be wait for the \
            visibility of element. The default value is 30 seconds. \n
        Example: \n\t\t time=30

    ----------

    Output
    ----------
    None

    """
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
    """
    Definition
    ----------
    Finds all elements with location similar of the \
        selector parameter
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    browser.find_elements(By.CSS_SELECTOR, selector)
    center_element(selector)


def find_element(selector):
    """
    Definition
    ----------
    Finds one element with the exact match location of \
        the selector parameter
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    browser.find_elements(By.CSS_SELECTOR, selector)
    center_element(selector)


def counter_elements(selector):
    """
    Definition
    ----------
    Counts all elements with location similar of the \
        selector parameter
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    elements = browser.find_elements(By.CSS_SELECTOR, selector)
    center_element(selector)
    return elements.__len__()


def extract_text(selector):
    """
    Definition
    ----------
    Extracts the text anchored in the element.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    element = browser.find_element(By.CSS_SELECTOR, selector)
    text_element = element.text
    center_element(selector)
    return text_element


def click_element(selector):
    """
    Definition
    ----------
    Click in the element informed with the exact match location of \
        the selector parameter.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    try:
        center_element(selector)
        element = browser.find_element(By.CSS_SELECTOR, selector)
        element.click()
        wait_page_loaded()
    except:
        ...


def write_in_element(selector, text):
    """
    Definition
    ----------
    Writes in the element informed with the exact match location of \
        the selector parameter.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    center_element(selector)
    element = browser.find_element(By.CSS_SELECTOR, selector)
    element.send_keys(text)
    wait_page_loaded()


def mouse_click(webelement):
    """
    Definition
    ----------
    Performs double left click of mouse in the webelement.
    Require to inform webelement parameter.

    ----------

    Parameters
    ----------
    webelement : WebDriver
        A webelement of the type WebDriver of Selenium library. \n
        Example: \n\t\t browser.find_element(\
            By.XPATH("//input[@value='submit']"))


    ----------

    Output
    ----------
    None

    """
    action = ActionChains(browser)
    action.double_click(webelement).perform()


def stop_browser():
    """
    Definition
    ----------
    Stops the Firefox browser controlled by automation.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    browser.close()
