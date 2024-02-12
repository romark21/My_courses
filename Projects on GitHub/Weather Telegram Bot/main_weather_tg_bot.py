import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types, Dispatcher, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import asyncio

from bs4 import BeautifulSoup
from time import sleep
import re

bot = Bot(token=tg_bot_token)
dp = Dispatcher()
# parse_mode='HTML'

inline_btn_1 = InlineKeyboardButton(text='Узнать погоду', callback_data='button1')
inline_btn_2 = InlineKeyboardButton(text='E-klasse', callback_data='button2')
inline_btn_3 = InlineKeyboardButton(text='SS.com', callback_data='button3')
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[inline_btn_1],
                     [inline_btn_2],
                     [inline_btn_3]]
)


@dp.message(Command('start'))
async def start_command(message: Message):
    await message.reply(f'🙋‍♂️<b>Привет, {message.from_user.first_name}!</b>\n'
                        '<em>Я бот, выбери что ты хочешь, нажав на одну из кнопок ниже!</em>',
                        reply_markup=keyboard,
                        parse_mode='HTML')
    # await message.delete()


@dp.callback_query(F.data == 'button1')
async def proces_button_1_press(callback: CallbackQuery):
    await callback.message.edit_text("Напиши мне названия города и я пришлю тебе сводку погоды.\n"
                                     "Название города пиши 'Латинскими' буквами:\n"
                                     )

    @dp.message()
    async def get_weather(message: Message):
        try:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
            )
            data = r.json()

            city = data["name"]
            cur_weather = data["main"]["temp"]
            feels_like_temp = data["main"]["feels_like"]
            humidity = data['main']["humidity"]
            pressure = data['main']["pressure"]
            temp_min = data['main']["temp_min"]
            temp_max = data['main']["temp_max"]
            wind = data['wind']["speed"]
            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_the_day = datetime.datetime.fromtimestamp(
                data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                data["sys"]["sunrise"])

            await callback.message.edit_text(
                f"Погода в городе:  <em>{city}</em>\nТемпература воздуха: <em>{cur_weather}°C</em>\n"
                f"По ощущениям:  <em>{feels_like_temp}°C</em>\n"
                f"Влажность воздуха:  <em>{humidity}%</em>\n"
                f"Давление воздуха:  <em>{pressure} мм рт.ст.</em>\n"
                f"Минимальная температура сегодня:  <em>{temp_min}°C</em>\n"
                f"Максимальная температура сегодня:  <em>{temp_max}°C</em>\n"
                f"Скорость ветра:  <em>{wind} м/c</em>\n"
                f"Восход солнца:  <em>{sunrise_timestamp}</em>\n"
                f"Заход солнца:  <em>{sunset_timestamp}</em>\n"
                f"Продолжительность светового дня:  <em>{length_of_the_day}</em>\n"
                f"\n<b>Введите названия города:</b>", reply_markup=keyboard, parse_mode='HTML'
            )
            # await message.delete()

        except:
            await callback.message.edit_text(
                "Проверьте правильность написание названия города!\nВведите названия города: ")


@dp.callback_query(F.data == 'button2')
async def proces_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text("<b>Извините</b>, <em>данный раздел на стадии разработки</em>",
                                     reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query(F.data == 'button3')
async def proces_button_3_press(callback: CallbackQuery):
    await callback.message.edit_text(f'{"-" * 10}\nAlfa Romeo, Audi\n{"-" * 40}\n'
                                     f'BMW\n{"-" * 40}\n'
                                     f'Chevrolet, Chrysler, Citroen\n{"-" * 40}\n'
                                     f'Dacia, Dodge\n{"-" * 40}\n'
                                     f'Fiat, Ford\n{"-" * 40}\n'
                                     f'Honda, Hyundai\n{"-" * 40}\n'
                                     f'Infiniti\n{"-" * 40}\n'
                                     f'Jaguar, Jeep\n{"-" * 40}\n'
                                     f'Kia\n{"-" * 40}\n'
                                     f'Lancia, Land Rover, Lexus\n{"-" * 40}\n'
                                     f'Mazda, Mercedes, Mini, Mitsubishi\n{"-" * 40}\n'
                                     f'Nissan\n{"-" * 40}\n'
                                     f'Opel\n{"-" * 40}\n'
                                     f'Peugeot, Porsche\n{"-" * 40}\n'
                                     f'Renault\n{"-" * 40}\n'
                                     f'Saab, Seat, Skoda, Smart, Subaru, Suzuki\n{"-" * 40}\n'
                                     f'Toyota\n{"-" * 40}\n'
                                     f'Volkswagen, Volvo\n{"-" * 40}\n'
                                     f'Vaz, Gaz, Uaz\n{"-" * 40}\n'
                                     f'Others\n{"-" * 10}\n'
                                     f'\nВведите марку автомобиля:')

    @dp.message()
    async def get_ss_parser(message: Message):
        headers = {"User-Agent":
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
        description_list = []

        def get_url():
            count = 1
            while count <= 1:
                url = f'https://www.ss.com/ru/transport/cars/{message.text}/page{count}.html'
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'lxml')
                data = soup.find_all('div', class_='d1')
                count += 1
                for i in data:
                    card_url = i.find('a')
                    if not card_url:
                        continue
                    url = 'https://www.ss.lv' + card_url.get('href')
                    yield url

        for i, url in enumerate(get_url(), 1):
            response = requests.get(url, headers=headers)
            sleep(3)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', {'id': 'content_main_div'})

            try:
                year = data.find('td', {'id': 'tdo_18'}).text
            except AttributeError:
                year = "--------"

            try:
                model = data.find('td', {'id': 'tdo_31'}).text
            except AttributeError:
                model = "--------"

            try:
                motor = data.find('td', {'id': 'tdo_15'}).text
            except AttributeError:
                motor = "--------"

            try:
                transmission = data.find('td', {'id': 'tdo_35'}).text
            except AttributeError:
                transmission = "--------"

            try:
                car_mileage = data.find('td', {'id': 'tdo_16'}).text
            except AttributeError:
                car_mileage = "--------"

            try:
                color = data.find('td', {'id': 'tdo_17'}).text
            except AttributeError:
                color = "--------"

            try:
                car_body = data.find('td', {'id': 'tdo_32'}).text
            except AttributeError:
                car_body = "--------"

            try:
                technical_inspection = data.find('td', {'id': 'tdo_223'}).text
            except AttributeError:
                technical_inspection = "--------"

            try:
                photo_url = data.find('div', class_='pic_dv_thumbnail').find('a').get('href')
            except AttributeError:
                photo_url = "--------"

            del_str = data.text.find('Марка')
            description = re.sub("^\s+|\n|\r|", '', data.text[:del_str])

            if description in description_list:
                continue
            else:

                if len(description) > 4000:
                    continue
                    # for x in range(0, len(description), 1000):
                    #     await message.answer(message.chat.id,
                    #                          f'{i})\nМодель: {model}\n{"-" * 20}\n'
                    #                          f'Год выпуска: {year}\n{"-" * 20}\n'
                    #                          f'Двигатель: {motor}\n{"-" * 20}\n'
                    #                          f'КПП: {transmission}\n{"-" * 20}\n'
                    #                          f'Тип кузова: {car_body}\n{"-" * 20}\n'
                    #                          f'Цвет: {color}\n{"-" * 20}\n'
                    #                          f'Пробег: {car_mileage} км.\n{"-" * 20}\n'
                    #                          f'Тех.Осмотр: {technical_inspection}\n{"-" * 20}\n')
                    #     await bot.send_message(message.chat.id, description[x:x + 1000])
                    #     await message.answer(message.chat.id, f'{url}\n{"-" * 60}\n')
                    # split_text = [description[i:i + 400] for i in range(0, len(description), 400)]
                    # await message.answer(message.chat.id,
                    #                      f'{i})\nМодель: {model}\n{"-" * 20}\n'
                    #                      f'Год выпуска: {year}\n{"-" * 20}\n'
                    #                      f'Двигатель: {motor}\n{"-" * 20}\n'
                    #                      f'КПП: {transmission}\n{"-" * 20}\n'
                    #                      f'Тип кузова: {car_body}\n{"-" * 20}\n'
                    #                      f'Цвет: {color}\n{"-" * 20}\n'
                    #                      f'Пробег: {car_mileage} км.\n{"-" * 20}\n'
                    #                      f'Тех.Осмотр: {technical_inspection}\n{"-" * 20}\n')
                    # for part in split_text:
                    #     await message.answer(message.chat.id,f'Описание: {part}')
                    # await message.answer(message.chat.id, f'{url}\n{"-" * 60}\n')
                    # for x in range(0, len(description), 4096):
                    # await bot.send_message(message.chat.id, description[x:x + 4096])
                else:
                    await bot.send_message(message.chat.id,
                                           f'{i})\nМодель: {model}\n{"-" * 20}\n'
                                           f'Год выпуска: {year}\n{"-" * 20}\n'
                                           f'Двигатель: {motor}\n{"-" * 20}\n'
                                           f'КПП: {transmission}\n{"-" * 20}\n'
                                           f'Тип кузова: {car_body}\n{"-" * 20}\n'
                                           f'Цвет: {color}\n{"-" * 20}\n'
                                           f'Пробег: {car_mileage} км.\n{"-" * 20}\n'
                                           f'Тех.Осмотр: {technical_inspection}\n{"-" * 20}\n'
                                           f'Описание: {description}\n{url}\n{"-" * 60}\n'
                                           f'Ссылка на фото автомобиля: {photo_url}\n{"-" * 60}\n')
                description_list.append(description)
                # description_file = open("список.json", "w", encoding="utf-8") as file:


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
