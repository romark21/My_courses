from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

driver = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)

    number = driver.find_element(By.ID, 'input_value').text

    answer = driver.find_element(By.XPATH, "//input[@id='answer']")
    answer.send_keys(calc(number))

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Делаем прокрутку страницы вниз

    checkbox = driver.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    checkbox.click()

    radiobutton = driver.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    sleep(4)

finally:
    driver.quit()

