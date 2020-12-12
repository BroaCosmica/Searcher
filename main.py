from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

links = [
    "todamateria.com.br",
    "brasilescola.uol.com.br",
    "infoescola.com",
    "mundoeducacao.uol.com.br"
] #links a serem pesquisados (Podem ser parcias)

request = input(": ")

service = Service(r".\chromedriver.exe")
service.start()

driver = webdriver.Remote(service.service_url) # driver = webdriver.Chrome()
driver.get("https://www.google.com.br/")


elem = driver.find_elements_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
elem[0].send_keys(request)
elem[0].send_keys(Keys.ENTER)


for site in links:
    elem = driver.find_elements_by_partial_link_text(site)
    elem[0].send_keys(Keys.CONTROL + Keys.ENTER)