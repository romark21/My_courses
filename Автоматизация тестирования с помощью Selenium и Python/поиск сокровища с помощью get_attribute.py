from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    driver.get('http://suninjuly.github.io/get_attribute.html')
    time.sleep(2)

    treasure = driver.find_element(By.ID, 'treasure')
    value = treasure.get_attribute('valuex')
    result = calc(value)

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(result)

    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    robots_rule = driver.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()
    time.sleep(5)

finally:
    driver.quit()
