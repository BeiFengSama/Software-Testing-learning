# iframe和frame切换的特殊处理
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, 'iframe'))
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')
for element in elements:
    print(element.get_attribute("innerHTML"))
# 切回主HTML
wd.switch_to.default_content()
wd.find_element(By.CSS_SELECTOR, '#outerbutton').click()
input()
