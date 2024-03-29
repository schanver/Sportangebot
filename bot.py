from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import datetime

info = []
kurs_id =  {"montag":'BS_Kursid_92577',"dienstag":'BS_Kursid_92578',"mittwoch":'BS_Kursid_92579',"donnerstag":'BS_Kursid_92580',"freitag":'BS_Kursid_92581'}
def read_from_file():
    with open('credentials.txt', 'r') as file:
        for line in file:
            info.append(line.strip())

def book_a_reservation(day):

    read_from_file()
    today = datetime.datetime.today()


    browser = webdriver.Firefox()

    vorname = info[0]
    familienname = info[1]
    strasse_nr = info[2]
    plz_ort = info[3]
    email = info[4]
    telefon = info[5]
    matrikelnummer = info[6]

    try:

        browser.get('https://www.buchsys.ahs.tu-dortmund.de/angebote/aktueller_zeitraum/_Basketball.html')
     
        WebDriverWait(browser,3).until(EC.title_contains('Sportangebot - HSP - TU Dortmund'))

        btn_name  = f"//input[@name='{kurs_id[day]}' and @class='bs_btn_buchen']"
        booking_button = browser.find_element(By.XPATH,btn_name)

        booking_button.click()

        #Switch the tabs 
        windows = browser.window_handles
        new_window = [window for window in windows if window != browser.current_window_handle][0]
        browser.switch_to.window(new_window)


        second_button = WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="inlbutton buchen" and @value="buchen"]')))
        second_button.click()

        gender_button = WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'//input[@class="bs_fval_req" and @value="M"]'))) 
        gender_button.click()

        name = browser.find_element(By.XPATH, '//input[@class="bs_form_field bs_fval_name" and @name="vorname"]')
        name.send_keys(vorname)
        
        surname = browser.find_element(By.XPATH, '//input[@class="bs_form_field bs_fval_name" and @name="name"]')
        surname.send_keys(familienname)

        street = browser.find_element(By.XPATH, '//input[@class="bs_form_field bs_fval_req" and @name="strasse"]')
        street.send_keys(strasse_nr)

        location = browser.find_element(By.XPATH, '//input[@class="bs_form_field bs_fval_ort" and @name="ort"]')
        location.send_keys(plz_ort)

        status = Select(browser.find_element(By.ID, 'BS_F1600'))
        status.select_by_index(1)

        matrikel_nr = browser.find_element(By.ID, 'BS_F1700')
        matrikel_nr.send_keys(matrikelnummer)

        mail = browser.find_element(By.ID, 'BS_F2000')
        mail.send_keys(email)
        
        phone_number = browser.find_element(By.ID, 'BS_F2100')
        phone_number.send_keys(telefon)

        checkbox = browser.find_element(By.NAME, 'tnbed')
        checkbox.click()
        

        #browser.execute_script("window.scrollBy(0,200);")
        browser.implicitly_wait(8)
        submit_button = browser.find_element(By.XPATH, '//input[@id="bs_submit" and @class="sub" and @value="weiter zur Buchung"]')
        submit_button.click()

        submit = browser.find_element(By.XPATH, '//input[@class="sub" and @title="binding reservation"]')
        submit.click()

        browser.implicitly_wait(3)
        browser.save_screenshot("reservation.png")
        print(f"Für {day[0].upper() + day[1:]} erfolgreich einen Platz reserviert")

    except NoSuchElementException as e:
        print(f"Exception occured: {e}")

    finally:
        browser.quit()
