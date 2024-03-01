# 通过tag选择元素
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
# 根据 tag name 选择元素，返回的是 一个列表
# 里面 都是 tag 名为 div 的元素对应的 WebElement对象
elements = wd.find_elements(By.TAG_NAME, 'div')
for element in elements:
    print(element.text)
input()

"""
find_element 和 find_elements 的区别
使用 find_elements 选择的是符合条件的 所有 元素， 如果没有符合条件的元素， 返回空列表
使用 find_element 选择的是符合条件的 第一个 元素， 如果没有符合条件的元素， 抛出 NoSuchElementException 异常
"""
