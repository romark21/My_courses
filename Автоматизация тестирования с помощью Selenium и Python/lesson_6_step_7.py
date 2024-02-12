import time
from selenium import webdriver
from selenium.webdriver.common.by import By

""""�� ���� ��� ������������� ������������ ������ �������� �� XPath. 

�� �������� http://suninjuly.github.io/find_xpath_form �� ������� ����� �� ����� �����������, ��� � ���� 3,
 ��� ���� � ��� ���������� ���� ���������� ������ ��������. �� ��������� ������ ������ � ������� "Submit",
  � ���� ������ ������ � ���� ������ �� ��. 

���� ����: 

� ���� �� ���� 4 �������� ������ ��  http://suninjuly.github.io/find_xpath_form.
��������� ���������� XPath-�������� ���, ����� �� ������� ������ ������ � ������� Submit.
 XPath ������ ������������� ��� ������ (�� ������, �� ���������, �� ���������) - �������, ����� �� �������.
������������� ��� �� ���� 3 ����� �������, ����� ����� ������ ���������� � ������� XPath.
��������� ��� ���.
���� �� ��������� ���������� �������� � ��� ������ ������, �� �� �������� ���,
 ������� ����� ��������� � �������� ������ �� ��� �������.
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
