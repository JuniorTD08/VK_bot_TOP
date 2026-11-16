from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor  # 1. Добавили импорт клавиатуры

import config
from kinopoisk_API import KinopoiskApi

vk_session = VkApi(token=config.VK_API_KEY)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
kinopisk = KinopoiskApi()


# 2. Функция создания клавиатуры со всеми командами
def get_main_keyboard():
    keyboard = VkKeyboard(one_time=False)  # one_time=False — кнопки не исчезают после нажатия

    # Первый ряд кнопок
    keyboard.add_button('/hello', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('/help', color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()  # Перенос на новую строку

    # Второй ряд кнопок
    keyboard.add_button('/random', color=VkKeyboardColor.SECONDARY)

    return keyboard.get_keyboard()


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        user_message: str = event.text

        if user_message.startswith("/hello"):
            message = "Приветствую!!!"
        elif user_message.startswith("/help"):
            message = "Чем могу вам помочь?\nНапишите /search название_фильма, чтобы найти кино."
        elif user_message == "/random":
            message = str(kinopisk.random_film())
        elif user_message.startswith("/search"):
            film_name = user_message[8:]
            message = str(kinopisk.search_film(film_name))
        else:
            message = "Я не знаю такую команду! Выберите команду на клавиатуре ниже."

        # 3. Передаем клавиатуру в параметр keyboard
        vk.messages.send(
            user_id=user_id,
            message=message,
            random_id=0,
            keyboard=get_main_keyboard()
        )

