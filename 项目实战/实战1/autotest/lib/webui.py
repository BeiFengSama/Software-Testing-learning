from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


def login_check(username, password):
    wd = webdriver.Chrome(service=Service())
    wd.get('http://127.0.0.1/mgr/sign.html')
    name = wd.find_element(By.CSS_SELECTOR, '#username')
    pwd = wd.find_element(By.CSS_SELECTOR, '#password')
    if username is not None:
        name.send_keys(username)
    if password is not None:
        pwd.send_keys(password)
    wd.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary btn-block btn-flat']").click()
    sleep(2)
    alert_text = wd.switch_to.alert.text
    wd.quit()
    return alert_text
