# 获取元素属性
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://www.byhy.net/_files/stock1.html')
element = wd.find_element(By.ID, '1')
print(element.get_attribute('class'))
