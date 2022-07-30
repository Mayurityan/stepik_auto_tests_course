from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
    for element in elements:
        if element.get_attribute('required') != None:
            element.send_keys("Мой ответ")

    print(os.getcwd())
    current_dir = os.path.realpath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)
    
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

