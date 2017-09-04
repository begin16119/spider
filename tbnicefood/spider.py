from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
browser = webdriver.Chrome()


def search():
    browser.get("https://www.taobao.com")
    input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
    )
    submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR,''))
