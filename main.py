import lib.selenium_utils as selenium
import lib.python_functions_utils as custom
import os
import datetime as dt
from time import sleep

try:
    try:
        message_error = ''
        current_date = dt.datetime.now().strftime('%d/%m/%Y').replace('/', '_')
        execution_initial = dt.datetime.now().strftime('%H:%M:%S')
        current_day_folder = current_date
        export_folder = 'export'
        log_folder = 'log'
        root_path = '.\\'+'files'+'\\'
        current_day_path = (
            root_path+'\\'+current_day_folder+'\\'
        )
        export_path = (
            root_path+'\\'+current_day_folder+'\\'+export_folder+'\\'
        )
        log_path = (
            root_path+'\\'+current_day_folder+'\\'+log_folder+'\\'
        )
        csv_file_name = 'series_list_exported.csv'
        log_name = 'log_'+current_date+'.txt'
        log_file = log_path + log_name
        csv_file = export_path + csv_file_name

        custom.create_directory(root_path)
        custom.create_directory(current_day_path)
        custom.create_directory(export_path)
        custom.create_directory(log_path)
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the initial process: Preparing the environment."
            )
        raise message_error

    try:
        # OPEN THE BROWSE WITH A URL
        url = "https://www.viki.com/"
        selenium.start_browser(url)
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 1: Starting browser."
            )
        raise message_error

    try:
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
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in Process 2: Logging to the web application."
            )
        raise message_error

    try:
        # CLICK IN "EXPLORER" LINK ON TOP OF MENU HORIZONTAL
        selector = "a[href="+"'/explore'"+"]"
        selenium.wait_element(selector)
        selenium.find_element(selector)
        selenium.click_element(selector)

        # INITIALIZE THE VARIABLES FOR LOGIC
        current_format_selection = ''
        tentatives = 1
        maximum_tentatives = 5
        while tentatives <= maximum_tentatives:
            # SHOW ALL TV SERIES FORMATS
            selector = 'div#s2id_type > a > span.select2-arrow > b'
            selenium.find_element(selector)
            selenium.click_element(selector)

            # DEFINE "TV" OPTION AS SERIE FORMAT SELECTIONED
            selector = "div#select2-drop > \
                ul[role="+"listbox"+"] > li:nth-child(2)"
            selenium.wait_element(selector)
            selenium.find_element(selector)
            selenium.click_element(selector)
            sleep(3)

            # STORE THE SELECTIONED REGION
            selector = 'div#s2id_type > a > span#select2-chosen-12'
            current_format_selection = selenium.extract_text(selector)

            # CONDITION FOR THE LOOP'S LOGIC
            tentatives = tentatives + 1

            # IF THE SELECTIONED REGION MATCH WITH THE OPTION REQUESTED
            if current_format_selection.upper().__contains__('TV'):
                # EXIT OF THE LOOP
                break
            # IF THE SELECTIONED REGION NOT MATCH WITH THE OPTION REQUESTED
            else:
                # WAIT 1 SECOUND
                sleep(1)
                if tentatives > maximum_tentatives:
                    message_error = TypeError(
                        "[Internal Business Error]: \
                            Error trying to select TV series format."
                    )
                    raise message_error

        # INITIALIZE THE VARIABLES FOR LOGIC
        current_country_selection = ''
        tentatives = 1
        maximum_tentatives = 5
        while tentatives <= maximum_tentatives:
            # SHOW ALL ORIGIN'S COUNTRY OPTIONS
            selector = 'div#s2id_country > a > span.select2-arrow > b'
            selenium.find_element(selector)
            selenium.click_element(selector)

            # DEFINE THE COUNTRY OPTION AS KOREA
            selector = "div#select2-drop > ul > \
                li[role="+"presentation"+"] > ul.select2-result-sub > \
                li[role="+"presentation"+"]:nth-child(2) > \
                div[class="+"select2-result-label"+"]"
            selenium.wait_element(selector)
            selenium.find_element(selector)
            selenium.click_element(selector)
            sleep(3)

            # STORE THE SELECTIONED REGION
            selector = "div#s2id_country > \
                a[class="+"select2-choice"+"] > \
                span[class="+"select2-chosen"+"]"
            current_country_selection = selenium.extract_text(selector)

            # CONDITION FOR THE LOOP'S LOGIC
            tentatives = tentatives + 1

            # IF THE SELECTIONED REGION MATCH WITH THE OPTION REQUESTED
            if current_country_selection.upper().__contains__('KOREA'):
                # EXIT OF THE LOOP
                break
            # IF THE SELECTIONED REGION NOT MATCH WITH THE OPTION REQUESTED
            else:
                # WAIT 1 SECOUND
                sleep(1)
                if tentatives > maximum_tentatives:
                    message_error = TypeError(
                        "[Internal Business Error]: \
                            Error trying to select TV series country."
                    )
                    raise message_error

        # INITIALIZE THE VARIABLES FOR LOGIC
        current_order_selection = ''
        tentatives = 1
        maximum_tentatives = 5
        while tentatives <= maximum_tentatives:
            # SHOW ALL SERIES ORDER OPTIONS
            selector = 'div.explore-sort-items > \
                div > a > span:nth-child(2) > i'
            selenium.wait_element(selector)
            selenium.find_element(selector)
            selenium.click_element(selector)

            # DEFINE THE SELECTIONED SERIES ORDER AS "POPULAR-ALL TIME"
            selector = 'div.explore-sort-items > \
                div > ul > li:nth-child(1) > a'
            selenium.wait_element(selector)
            selenium.find_element(selector)
            selenium.click_element(selector)
            sleep(3)

            # STORE THE SELECTIONED SERIES ORDER
            selector = "div.explore-sort-items > div > a > span:nth-child(2)"
            current_order_selection = selenium.extract_text(selector)

            # CONDITION FOR THE LOOP'S LOGIC
            tentatives = tentatives + 1

            # IF THE SELECTIONED SERIES ORDER MATCH WITH THE OPTION REQUESTED
            if current_order_selection.upper().__contains__(
                'POPULAR - ALL TIME'
            ):
                # EXIT OF THE LOOP
                break
            # IF THE SELECTIONED SERIES ORDER NOT
            #       MATCH WITH THE OPTION REQUESTED
            else:
                # WAIT 1 SECOUND
                sleep(1)
                if tentatives > maximum_tentatives:
                    message_error = TypeError(
                        "[Internal Business Error]: \
                            Error trying to select TV series order list."
                    )
                    raise message_error
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 3: filtering series list on webpage."
            )
        raise message_error

    try:
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

            # WAIT THE GENERAL ELEMENT OF ELEMENT'S
            #       LIST TO BE AVALIABLE IN THE SCREEN
            selector = 'div.row-inline > div.thumbnail'
            selenium.wait_element(selector)

            # STORE THE LENGTH OF SERIES AVALIABLES IN THE PAGE
            counter_series = selenium.counter_elements(selector)

            # FOR EACH SERIE IN THE PAGE
            while counter_current <= counter_series:
                # DEFINE THE LOGIC LOCAL OF THE SERIE
                selector = "div.row-inline > div.thumbnail:nth-child(" \
                    + str(counter_current) + \
                    ") > div[class=" + \
                    "'thumbnail-description dropdown-menu-wrapper'" + \
                    "] > div > a"

                # WAIT THE CURRENT SERIE BE AVALIABLE IN THE PAGE
                selenium.wait_element(selector)

                # FINDS CURRENT SERIE
                selenium.find_element(selector)

                # STORE THE NAME OF SERIE AND SAVE IT IN THE LIST
                list_all_titles_movies_saved.append(
                    selenium.extract_text(selector)
                )

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
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 4: \
                    Extracting series names for internal list."
            )
        raise message_error

    try:
        # DEFINE THE HEADER OF FILE'S EXPORT .CSV
        custom.save_csv(csv_file, 'w', ["Nome da série"])

        # EXPORTS THE SERIES LIST FOR THE FILE .CSV
        custom.save_csv(
            csv_file,
            'a',
            custom.serie_list_handling(list_all_titles_movies_saved)
        )
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 5: \
                    Extract of series list to export .csv file."
            )
        raise message_error

except:
    if not str(message_error).__contains__('[Internal Business Error]'):
        message_error = '[Internal System Error]: ' + str(message_error)
    status = 'NOK'
    message = message_error

finally:
    try:
        # CLOSE THE BROWSER
        selenium.stop_browser()
        ...
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the final process: Stopping the browser."
            )

    if message_error == '':
        status = 'OK'
        message = 'Process have been done with success.'

    current_time_log = dt.datetime.now().strftime('%H:%M:%S')
    file_exists = os.path.exists(log_file)
    if not file_exists:
        custom.save_csv(log_file, 'w', [
            'Status ',
            'Message Execution ',
            'DateTime Initial Execution ',
            'Time Final Execution '
        ])
    log = open(log_file, 'a', encoding='utf8')
    log_content = (
        status,
        message,
        current_date.replace('_', '/') + ': ' + execution_initial,
        current_time_log
    )
    log_content = str(
        log_content
    ).replace('(', '').replace(')', '').replace('TypeError', '')
    log.write(log_content + '\r\n')
    log.close()
