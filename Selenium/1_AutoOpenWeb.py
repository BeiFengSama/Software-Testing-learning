# 自动化打开网址
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 创建webDriver对象
wd = webdriver.Chrome(service=Service())
wd.get('https://www.baidu.com')
input()
