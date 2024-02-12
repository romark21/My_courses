import time
from selenium import webdriver
from selenium.webdriver.common.by import By

""""Ќа этот раз воспользуемс€ возможностью искать элементы по XPath. 

Ќа странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3,
 при этом в нее добавилась куча одинаковых кнопок отправки. Ќо сработает только кнопка с текстом "Submit",
  и наша задача нажать в коде именно на неЄ. 

¬аши шаги: 

¬ коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
ѕодберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit.
 XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
ћодифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
«апустите ваш код.
≈сли вы подобрали правильный селектор и все прошло хорошо, то вы получите код,
 который нужно отправить в качестве ответа на это задание.
"""


url = 'http://suninjuly.github.io/find_xpath_form'
driver = webdriver.Chrome()

try:
    driver.get(url)
    first_name = driver.find_element(By.TAG_NAME, "input")
    first_name.send_keys('Roman')

    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys("Pupkin")

    city = driver.find_element(By.CLASS_NAME, "city")
    city.send_keys("Riga")

    country = driver.find_element(By.ID, "country")
    country.send_keys("Latvia")

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
finally:
    time.sleep(5)
    driver.quit()
