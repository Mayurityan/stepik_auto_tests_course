from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
    str(int(x) + int(y))
    z = calc()

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    number_1 = browser.find_element(By.CSS_SELECTOR,"#num1")
    x = number_1.text
    number_2 = browser.find_element(By.CSS_SELECTOR,"#num2")
    y = number_2.text
    z = int(x) + int(y)

    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
