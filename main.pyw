import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from kivy_window import MyApp
import chromedriver_autoinstaller



with open("links.json", "r") as json_file:
    links = json.load(json_file)


kivy_app = MyApp()
kivy_app.run()

request = kivy_app.researcher()


chromedriver_autoinstaller.install()

# service = Service(r"./chromedriver.exe")
# service.start()


driver = webdriver.Chrome()
driver.get("https://www.google.com.br/")


elem = driver.find_elements_by_xpath(
    '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
elem[0].send_keys(request)
elem[0].send_keys(Keys.ENTER)


for site in links["normal links"]:
    elem = driver.find_elements_by_partial_link_text(site)
    if elem != []:
        sleep(1.5)
        elem[0].send_keys(Keys.CONTROL + Keys.ENTER)
