def text_info(data):
    print(data)
    message = (f"Имя: {data["name"]}\n"
               f"Год: {data["year"]}\n"
               f"Описание: {data["disc"]}\n")
    return message

film = {
    "name": "text_1",
    "year": "text_2",
    "disc": "text_3"
}

text_info(text= film)
