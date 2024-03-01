# 通过css选择器选择属性来选择元素
# css 选择器支持通过任何属性来选择元素，语法是用一个方括号 []
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
element = wd.find_element(By.CSS_SELECTOR, '[href$="gov.cn"]')
print(element.get_attribute('outerHTML'))
texts = wd.find_elements(By.CSS_SELECTOR, 'div[class=animal]')
for i in texts:
    print(i.text)
