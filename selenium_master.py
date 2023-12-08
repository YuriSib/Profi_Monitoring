import time
from twocaptcha import TwoCaptcha
import sys
import os
from bs4 import BeautifulSoup
import urllib.request

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


solver = TwoCaptcha('791a1c2ea34bdead3918fffa46003ad6')

s = Service(executable_path='C:\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get('https://profi.ru/backoffice/n.php')
    username_input = driver.find_element("xpath", '''//*[@id="content"]/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/label/span/input''')
    username_input.send_keys("+79381736854")
    button = driver.find_element("xpath", '''//*[@id="content"]/div/div[2]/div/div[2]/div/div/form/a''')
    button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", '''//*[@id="rc-imageselect-target"]/
    table/tbody/tr[2]/td[2]/div/div[1]/img''')))
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    pic = soup.find('div', class_="rc-image-tile-target")#.find('img')["src"]
    photo_saver(pic)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()