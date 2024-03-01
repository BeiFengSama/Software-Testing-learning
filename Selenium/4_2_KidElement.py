"""
直接子元素：element > element1  选择的是element1
ps:element > element1 >element2 > element3  选择的是element3
后代子元素：element element1 选择的是element1
ps:element   element1  element2   element3  选择的是element3
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
element = wd.find_element(By.CSS_SELECTOR, '#container #inner11 > span')
print(element.text)
