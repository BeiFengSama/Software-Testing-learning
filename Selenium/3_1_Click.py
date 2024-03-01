"""
调用元素WebElement对象的 click方法,浏览器接收到自动化命令，
点击的是该元素的 中心点 位置
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://www.byhy.net/_files/stock1.html')
form = wd.find_element(By.ID, 'kw')
form.send_keys('通讯')
button = wd.find_element(By.ID, 'go')
button.click()
elements = wd.find_elements(By.CLASS_NAME, 'name')
for element in elements:
    print(element.text)
