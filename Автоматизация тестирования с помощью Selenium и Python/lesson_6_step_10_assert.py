import time
from selenium import webdriver
from selenium.webdriver.common.by import By



url = 'http://suninjuly.github.io/registration1.html'
driver = webdriver.Chrome()


try:
    driver.get(url)

    first_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your first name']")
    first_name.send_keys('Roman')

    last_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your last name']")
    last_name.send_keys("Pupkin")

    email = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your email']")
    email.send_keys("romanpupkin@gmail.com")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    time.sleep(1)

    confirm = driver.find_element(By.TAG_NAME, 'h1').text
    assert 'Congratulations! You have successfully registered!' == confirm

finally:
    time.sleep(3)
    driver.quit()
