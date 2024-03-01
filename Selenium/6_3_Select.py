# 根据选项的 value属性值 ，选择元素:select_by_value('value')
# 根据选项的 次序 （从0开始），选择元素:select_by_index(n)
# 根据选项的 可见文本 ，选择元素:select_by_visible_text('value')
# 去除选中的选项，即把上述select改为deselect。但去除所有：deselect_all()
# _____________________________分割线___________________________________
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
# 单选框
single_select = Select(wd.find_element(By.CSS_SELECTOR, '#ss_single'))
single_select.select_by_visible_text('小雷老师')
# 复选框
select = Select(wd.find_element(By.CSS_SELECTOR, '#ss_multi'))
select.deselect_all()
select.select_by_visible_text('小雷老师')
select.select_by_visible_text('小凯老师')
input()
