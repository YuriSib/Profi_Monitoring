import time
import requests
import sys
import os
from bs4 import BeautifulSoup
import urllib.request
from twocaptcha import TwoCaptcha

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def photo_saver(url_):
    try:
        urllib.request.urlopen(url_)
    except urllib.error.URLError as e:
        print("Ошибка при скачивании фото:", e)
    else:
        try:
            with open(f'captcha.jpg', 'wb') as f:
                f.write(urllib.request.urlopen(url_).read())
                print("Фото успешно скачано!")
        except Exception:
            print("Ошибка при скачивании фото:")


def log_in():
    s = Service(executable_path='C:\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    # try:
    driver.maximize_window()
    driver.get('https://profi.ru/backoffice/n.php')
    username_input = driver.find_element("xpath", '''//*[@id="content"]/div/div[2]/div/div[2]/div/div/form/div/div
                                                                                        /div[1]/label/span/input''')
    username_input.send_keys("+79381736854")
    button = driver.find_element("xpath", '''//*[@id="content"]/div/div[2]/div/div[2]/div/div/form/a''')
    button.click()
    time.sleep(8)

    # element_for_delete = driver.find_element("css selector", "body > div:nth-child(17)")
    # driver.execute_script("arguments[0].remove()", element_for_delete)
    #
    # element_to_replace = driver.find_element("css selector", "#g-recaptcha-response")
    # driver.execute_script(f"var oldElement = document.querySelector('#g-recaptcha-response'); var newElement = document.createElement('input'); newElement.setAttribute('type', 'submit'); document.body.appendChild(newElement);")

    elem_hidden = driver.find_element("css selector", 'textarea.g-recaptcha-response')
    driver.execute_script("arguments[0].style.display = 'block';", elem_hidden)

    # response = requests.post("http://rucaptcha.com/in.php?key=791a1c2ea34bdead3918fffa46003ad6&method=userrecaptcha&"
    # "googlekey=6LfblGwnAAAAAIcKbojt23iwNJk3Tnh5Mk1Xq3m0&pageurl=https://profi.ru/backoffice/n.php").text.replace('OK|', '')
    # time.sleep(25)
    # token = requests.get(f"http://rucaptcha.com/res.php?key=791a1c2ea34bdead3918fffa46003ad6&action=get&id={response}").text.replace('OK|', '')
    # while token == 'CAPCHA_NOT_READY':
    #     time.sleep(5)
    #     token = requests.get(
    #         f"http://rucaptcha.com/res.php?key=791a1c2ea34bdead3918fffa46003ad6&action=get&id={response}").text.replace(
    #         'OK|', '')
    # # token = 'token'

    # element = driver.find_element("css selector", 'textarea.g-recaptcha-response')
    # driver.execute_script(f'''arguments[0].setAttribute('id', '{token}')''', element)

    # driver.execute_script(f'''document.getElementById("g-recaptcha-response").innerHTML="{token}"''')

    # form = driver.find_element("css selector", '''#content > div > div.WrapperStyles__ContentWrapper-sc-fpifz8-2.gWGsZR > div > div.auth-container > div > div > form''')
    # form.find_element("class name", 'login-form').send_keys('1342342')
    driver.execute_script('''document.getElementsByClassName("login-form").submit();''')
    print(token)
    time.sleep(20)


    # frame_list = driver.find_elements("tag name", "iframe")
    #
    # pic = None
    # cnt = 0
    # for frame in frame_list:
    #     cnt += 1
    #     driver.switch_to.default_content()
    #     driver.switch_to.frame(frame)
    #     html = driver.page_source
    #     soup = BeautifulSoup(html, "lxml")
    #     html_pic = soup.find('div', class_="rc-imageselect-challenge")
    #     if html_pic:
    #         pic = html_pic.find('img')["src"]
    #         break
    #
    # driver.switch_to.default_content()
    # html = driver.page_source
    # soup = BeautifulSoup(html, "lxml")
    # captcha_token = (soup.find_all('iframe')[cnt])["src"]
    # document.getElementById("recaptcha-demo-form").submit()
    #
    # if pic:
    #     photo_saver(pic)
    # token_captcha = html.find_element()


    # except Exception as ex:
    #     print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()


if __name__ == "__main__":
    log_in()
