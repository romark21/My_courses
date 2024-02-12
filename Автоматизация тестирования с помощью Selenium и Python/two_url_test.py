import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/registration1.html'
url_2 = 'http://suninjuly.github.io/registration2.html'
driver = webdriver.Chrome()


try:
    driver.get(url)

    first_name = driver.find_element(By.CSS_SELECTOR, ".first_block > .first_class > .first")
    first_name.send_keys('Roman')
    time.sleep(1)

    last_name = driver.find_element(By.CSS_SELECTOR, ".first_block > .second_class > .second")
    last_name.send_keys("Pupkin")
    time.sleep(1)

    email = driver.find_element(By.CSS_SELECTOR, ".first_block > .third_class > .third")
    email.send_keys("romanpupkin@gmail.com")
    time.sleep(1)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    time.sleep(1)

    confirm = driver.find_element(By.TAG_NAME, 'h1').text
    assert 'Congratulations! You have successfully registered!' == confirm

finally:
    time.sleep(2)
    driver.quit()

