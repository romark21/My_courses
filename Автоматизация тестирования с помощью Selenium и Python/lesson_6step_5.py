import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://suninjuly.github.io/huge_form.html'
driver = webdriver.Chrome()


try:
    driver.get(url)
    forms = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for id, form in enumerate(forms):
        form.send_keys(id)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    driver.quit()



