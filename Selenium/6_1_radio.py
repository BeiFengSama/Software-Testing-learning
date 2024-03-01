# radio选择框
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
check = wd.find_element(By.CSS_SELECTOR,
                        '#s_radio input[checked=checked]')
print(check.get_attribute('value'))
wd.find_element(By.CSS_SELECTOR, '#s_radio input[value=小雷老师]').click()
input()
