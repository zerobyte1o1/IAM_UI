from selenium import webdriver

import os
from selenium.webdriver.chrome.service import Service

chrome_driver = os.popen("where chromedriver").read()
print(chrome_driver)
s = Service(chrome_driver)
driver = webdriver.Chrome(service=s)

# driver=webdriver.Chrome()

