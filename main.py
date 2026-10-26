from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

import config

vk_session = VkApi(token=config.VK_API_KEY)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        user_id = event.user_id
        user_message: str = event.text

        if user_message.startswith("/hello"):
            message = "Hello "
        elif user_message.startswith("/help"):
            message = "Чем могу вам помочь?"
        else:
            message = "Я не знаю такую команду!"

        vk.messages.send(
            user_id=user_id,
            message=user_message,
            random_id=0
        )
