import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from kivy_window import Searcher


with open("links.json", "r") as json_file:
    links = json.load(json_file)

kivy_app = Searcher()
kivy_app.run()


request = kivy_app.researcher()

service = Service(r"./chromedriver.exe")
service.start()

driver = webdriver.Remote(service.service_url)
driver.get("https://www.google.com.br/")


elem = driver.find_elements_by_xpath(
    '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
elem[0].send_keys(request)
elem[0].send_keys(Keys.ENTER)


for site in links["normal links"]:
    elem = driver.find_elements_by_partial_link_text(site)
    elem[0].send_keys(Keys.CONTROL + Keys.ENTER)
    sleep(1.5)
