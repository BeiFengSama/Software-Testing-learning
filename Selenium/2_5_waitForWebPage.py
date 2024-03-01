# 等待页面加载
# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://www.byhy.net/_files/stock1.html')
element = wd.find_element(By.ID, 'kw')
element.send_keys('通讯\n')
element = wd.find_element(By.ID, '1')
print(element.text)
"""
出现异常抛出
selenium.common.exceptions.NoSuchElementException: Message: no such element:
Unable to locate element: {"method":"css selector","selector":"[id="1"]"}
意思就是在当前的网页上 找不到该元素， 就是找不到 id 为 1 的元素。
1、此时可以尝试Sleep(1)
2、Selenium 的 Webdriver 对象 有个方法叫 implicitly_wait ，可以称之为 隐式等待 ，或者 全局等待 。
注：implicitly_wait只有在找不到元素时会每隔0.5秒再找一次，但遇到重新加载时可能出现id存在但内容不为自己所需要的，此时仍然使用sleep
"""
