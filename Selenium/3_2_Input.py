# 输入框
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/test3.html')
element = wd.find_element(By.ID, 'input1')
element.clear()
element.send_keys('jhh')
input()
