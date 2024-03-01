from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
element = wd.find_element(By.CSS_SELECTOR, '#searchtext')
element.send_keys('hduahd')
print(element.get_attribute('value'))
