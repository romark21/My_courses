from time import sleep
import requests
from bs4 import BeautifulSoup
import fake_useragent
import re
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_diary_page_data():
    url = 'https://my.e-klase.lv/?v=15'
    user_agent = fake_useragent.UserAgent().random
    header = {'user-agent': user_agent}
    data = {
        'UserName': '211009-21492',
        'Password': 'j*paliek'
    }
    with requests.session() as session:
        session.get(url)
        response = session.post(url, data=data, headers=header)
        if response.status_code == 200:
            cookies = response.cookies.get_dict()
        else:
            print('Ошибка при отправке запроса для авторизации!')
        buttons_url = 'https://my.e-klase.lv/SessionContext/SwitchStudentWithFamilyStudentAutoAdd'
        response = session.get(buttons_url, cookies=cookies)
        if response.status_code == 200:
            cookies = response.cookies.get_dict()
        else:
            print('Ошибка при отправке запроса в окне выбора профиля!')
        diary = 'https://my.e-klase.lv/Family/Diary'
        diary = re.sub(r'>\s+<', '><', diary.replace('\n', ''))
        response = session.get(diary, cookies=cookies)
        if response.status_code == 200:
            cookies = response.cookies.get_dict()
        else:
            print('Ошибка при отправке запроса, вкладка - "Дневник"!')
        soup = BeautifulSoup(response.text, 'lxml')

        return soup

def get_diary_days_data():
    day_data = get_diary_page_data().find_all('table', class_='lessons-table')
    for i in day_data:
        data = i.find('tbody').find_all('tr')
        sleep(2)
        yield data

def get_day_data():
    data = []
    for i in get_diary_days_data():



        # lesson_name = i.find_all('span', class_='room')
        # for name in lesson_name:
        try:
            lesson_name = i.find('span', class_='title').text.strip()
            # lesson_name = lesson_name.previous_element.text.strip()
        except AttributeError:
            lesson_name = ''
        # yield lesson_name


        # lesson_topic = i.find_all('td', class_='subject')
        # for topic in lesson_topic[1:]:
        try:
            lesson_topic = i.find('td', class_='subject')
            lesson_topic = lesson_topic.text
        except AttributeError:
            lesson_topic = ''
            # yield lesson_topic

        # hometask = i.find_all('td', class_='hometask')
        # for task in hometask[1:]:
        try:
            hometask = i.find('td', class_='hometask').text
        except AttributeError:
            hometask = ''
            # yield hometask

        # score = i.find_all('td', class_='score')
        # for sc in score:
        try:
            score = i.find_all('td', class_='score')
            score = score.get('data-id')
        except AttributeError:
            score = ''
            # yield score
    # data.append
        result = (f'{lesson_name} --- Тема: {lesson_topic}  --- Домашнее задание: {hometask} --- Оценка: {score}')
        print(result)
get_day_data()
# def main():
#     # for i in get_day_data():
#     print(get_day_data())
#     print('---' * 10)
#
# if __name__ == "__main__":
#     main()