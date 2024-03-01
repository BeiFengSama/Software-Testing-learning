# 通过ID定位元素并输入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service())
wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw')
element.send_keys('通讯\n')
input()
