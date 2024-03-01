# 通过class选择一类元素并打印
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
# 获取的元素存入列表，.text输出文本信息
elements = wd.find_elements(By.CLASS_NAME, 'animal')
for element in elements:
    print('find_elements' + element.text)
# 去掉s，仅打印第一个class为animal的元素
element = wd.find_element(By.CLASS_NAME, 'animal')
print('find_element:' + element.text)
input()
