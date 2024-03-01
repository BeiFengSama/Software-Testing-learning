# radio选择框
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
checks = wd.find_elements(By.CSS_SELECTOR,
                          '#s_checkbox input[checked=checked]')
for check in checks:
    check.click()
wd.find_element(By.CSS_SELECTOR, '#s_checkbox input[value=小雷老师]').click()
input()
