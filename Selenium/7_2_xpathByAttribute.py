#  [@属性名='属性值']
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/test1.html')
elements = wd.find_elements(By.XPATH, '//select[@class="multi_choice"]')
for element in elements:
    print(element.get_attribute('innerHTML'))
"""
如果一个元素有多个class，那么需要选择全部class属性
<p id="beijing" class='capital huge-city'>北京</p>
如果要选 它， 对应的 xpath 就应该是 //p[@class="capital huge-city"]
不能只写一个属性，像这样 //p[@class="capital"] 则不行
"""
