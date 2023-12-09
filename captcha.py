import time

from python_rucaptcha.re_captcha import ReCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class FontDownloader:
    def __init__(self, token: str):
        self.s = Service(executable_path='C:\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)
        self.token = token

    def input_number(self):
        self.driver.get('https://profi.ru/backoffice/n.php')
        username_input = self.driver.find_element("xpath", '''//*[@id="content"]/div/div[2]/div/div[2]/div/div/form/
                                                  div/div/div[1]/label/span/input''')
        username_input.send_keys("+79381736854")
        self.driver.find_element("xpath", '''//*[@id="content"]/div/div[2]/div/div[2]/div/div/form/a''').click()
        time.sleep(3)

        self.driver.switch_to.frame(self.driver.find_elements("tag name", "iframe")[3])


        elem_hidden = self.driver.find_element("xpath", '''//*[@id="recaptcha-reload-button"]''')
        elem_hidden.click()
        time.sleep(5)

    def __solve_captcha(self):
        elem_hidden = self.driver.find_element("css selector", "#rc-imageselect")
        time.sleep(5)


FontDownloader(token='791a1c2ea34bdead3918fffa46003ad6').input_number()
