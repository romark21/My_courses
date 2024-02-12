# coding: utf8
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# <input class="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked="">

try:
    driver.get('http://suninjuly.github.io/math.html')

    people_radio = driver.find_element(By.ID, 'peopleRule')
    type_checked = people_radio.get_attribute('type')
    print(type_checked)
    # radio

    class_checked = people_radio.get_attribute('class')
    print(class_checked)
    # form-check-input

    check_checked = people_radio.get_attribute('checked')
    print(check_checked)
    # true

    find_a_nonexistent = people_radio.get_attribute('href')
    print(find_a_nonexistent)
    # None


finally:
    driver.quit()

# false будет ТОЛЬКО в том случае если "false" явно указано как значение атрибута, т.е. что-то типа value="false".
# Т.е. сам по себе метод get_attribute() false не возвращает в качестве одного из своих значений (например,
# на отсутствие атрибута или на отсутствие его значения)