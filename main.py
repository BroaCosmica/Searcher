from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep


request = input(": ")

service = Service(r".\chromedriver.exe")
service.start()

driver = webdriver.Remote(service.service_url) # driver = webdriver.Chrome()
driver.get("https://www.google.com.br/")

sleep(1)
elem = driver.find_elements_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input') #//*[@id="input"]
elem[0].send_keys(request[0:])
elem[0].send_keys(Keys.ENTER)

sleep(5)
#driver.close()