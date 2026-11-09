from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

import config

from kinopoisk_API import KinopoiskApi

vk_session = VkApi(token=config.VK_API_KEY)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
kinopisk = KinopoiskApi()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        user_id = event.user_id
        user_message: str = event.text

        if user_message.startswith("/hello"):
            message = "Пиветствую!!!"
        elif user_message.startswith("/help"):
            message = "Чем могу вам помочь?"
        elif user_message == "/random":
            message = str(kinopisk.random_film())
        elif user_message.startswith("/search"):
            film_name = user_message[8:]
            message = str(kinopisk.search_film(film_name))


        else:
            message = "Я не знаю такую команду!"


        vk.messages.send(
            user_id=user_id,
            message=message,
            random_id=0
        )
