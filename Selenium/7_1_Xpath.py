"""
一、绝对路径
绝对路径：html/body/div
等价于css表达式：html>body>div

xpath调用方法：find_element(By.XPATH, '路径')或find_elements(By.XPATH, '路径')

二、相对路径
xpath需要前面加 // , 表示从当前节点往下寻找所有的后代元素,不管它在什么位置
例：//div  查找所有div
//div//p    div里所有的p
//div/p   div的直接子元素p

三、通配符
//div/*  div下全部直接子元素
//div//*  div下全部元素
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/test1.html')
elements = wd.find_elements(By.XPATH, '//div//*')
for element in elements:
    print(element.get_attribute('outerHTML'))
