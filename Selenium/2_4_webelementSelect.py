# webElement可以选择element内部的元素
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
element = wd.find_element(By.ID, 'container')
# 选择element内部的span元素
span = element.find_element(By.TAG_NAME, 'span')
print(span.text)
input()
