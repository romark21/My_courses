import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

def get_url():  #Функция позволяет не создавать список с твароми
    count = 1
    while count < 7:
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"  #Отправляем запрос на сайт

        response = requests.get(url, headers = headers)  #Отправляем запрос на сайт
        soup = BeautifulSoup(response.text, 'lxml') #Разбираем данные при помощи Beatifulsop

        data = soup.find_all("div", class_="w-full rounded border") #По тегам находим информация не посредственно о карточке товара
        count += 1
        for i in data:
            # Берем Имя, Цену и ссылку на фото без открывания каждой карточки товара
            # name = i.find("h4").text.replace('\n', '')
            # price = i.find("h5").text.replace('\n', '')
            # info =
            # url_img = 'https://scrapingclub.com' + i.find('img', class_="card-img-top img-fluid").get('src')
            # print(name)
            # print(price)
            # print(url_img + '\n')
            card_url = "https://scrapingclub.com" + i.find("a").get("href") # Нашли и дополнили ссылку на карточку товара.
            yield card_url  #Ссылку передали на нижний For

for i, card_url in enumerate(get_url(), 1): #Перебераем ссылки с карточками товаров в созданном ранее списке.( For выше)
    response = requests.get(card_url, headers=headers) #Делаем get запрос, тоесть открываем каждую карточку
    sleep(3)
    soup = BeautifulSoup(response.text, 'lxml') #Разбираем данные при помощи Beatifulsop

    data = soup.find("div", class_="my-8 w-full rounded border") #Берём всю информацию о карточке твара по тегам
    name = data.find("h3", class_="card-title").text
    price = data.find("h4", class_="my-4 card-price").text
    description = data.find("p", class_="card-description").text
    url_img = "https://scrapingclub.com" + data.find("img").get("src")
    print(f'{i})\n {name}\n {price}\n {description}\n{url_img}')
    print()
