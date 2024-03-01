from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service())
wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')
# 父元素的第n个子节点:nth-child(n)
# 父元素的倒数第n个子节点:nth-last-child(n)
# 父元素的第几个某类型的子节点:nth-of-type(n)
# 父元素的倒数第n个某类型的子节点:nth-last-of-type(n)
# 奇数节点:nth-child(odd)
# 偶数节点:nth-child(even)
# 父元素的某类型偶数节点:nth-of-type(even)
# 父元素的某类型偶数节点:nth=of=type(odd)
# 相邻兄弟节点选择 h3 + span
# 后续所有兄弟节点选择 h3 ~ span
e1 = wd.find_elements(By.CSS_SELECTOR, '#t1 h3 ~')
for i in e1:
    print(i.text)
