# 切换到新页面
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')
wd.find_element(By.CSS_SELECTOR, 'a[href*="bing"]').click()
mainwindow = wd.current_window_handle
print(wd.title)
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if 'bing' in wd.title:
        break
print(wd.title)
wd.switch_to.window(mainwindow)
print(wd.title)
