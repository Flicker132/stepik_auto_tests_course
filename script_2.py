from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    time.sleep(5)
    alert = browser.switch_to.alert
    result = alert.text.split()[-1]
    print(f"Код для ответа: {result}")
    alert.accept()

finally:
    browser.quit()
