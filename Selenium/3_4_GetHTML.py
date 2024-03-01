# 通过get_attribute获取innerHTML和outerHTML
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://www.byhy.net/_files/stock1.html')
element = wd.find_element(By.ID, '1')
print(element.get_attribute('innerHTML'))
print(element.get_attribute('outerHTML'))
# 获取input输入框的内容（无法使用.text获取）
inp = wd.find_element(By.ID, 'kw')
inp.send_keys('jhh')
print(inp.get_attribute('value'))
"""
但是，有时候，元素的文本内容没有展示在界面上，或者没有完全完全展示在界面上。
这时，用WebElement对象的text属性，获取文本内容，就会有问题。
出现这种情况，可以尝试使用 element.get_attribute('innerText') ，
或者 element.get_attribute('textContent')
使用 innerText 和 textContent 的区别是，前者只显示元素可见文本内容，
后者显示所有内容（包括display属性为none的部分）
"""
