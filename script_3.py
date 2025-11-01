from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
    time.sleep(5)
    alert = browser.switch_to.alert
    result = alert.text.split()[-1]
    print(f"Код для ответа: {result}")
    alert.accept()

finally:
    browser.quit()
