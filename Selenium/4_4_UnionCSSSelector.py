# 联合选择
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
# wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
# 联合选择
element = wd.find_element(By.CSS_SELECTOR, '.footer1 .date')
print("联合选择: " + element.text)
# 组选择
elements = wd.find_elements(By.CSS_SELECTOR, '.animal, .plant')
for i in elements:
    print("组选择: " + i.text)

# 子元素里的组选择
wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')
elements = wd.find_elements(By.CSS_SELECTOR, '#t1 > span, #t1 > h3, #t1 > p')
for i in elements:
    print("子元素里的组选择: " + i.text)
"""
另外注意：组选择结果列表中，选中元素排序， 不是 组表达式的次序， 而是符合这些表达式的元素，在HTML文档中的出现的次序
"""
