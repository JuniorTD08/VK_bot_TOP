# Todo doc and ANOTATION, достать постер / isibjnstance read
import requests


class KinopoiskApi:

    BASE_URL = "https://kinopoisk.dev/v1.5/movie"
    HEADERS = {"X-API-KEY": "FKV6CYW-22G42TA-Q7B1MNV-658FP78"}

    def random_film(self):
        url = "https://api.poiskkino.dev/v1.5/movie/random"
        response = requests.get(url=url, headers=self.HEADERS)
        film = self.info(data=response.json())

        dict_film = self.info(data=film)
        message = self.text_info(data=dict_film)
        return message


    def info(self, data):
        name = data.get("name", "Не найдено!")
        year = data.get("year", "Год не найден")
        disc = data.get("description", "Не найдено!")

        film = {
            "name": name,
            "year": year,
            "disc": disc,
        }
        return film

    def search_films_name(self,name):
        url = f"https://api.poiskkino.dev/v1.5/movie/search?page=1&limit=10&query={name}"
        response = requests.get(url=url, headers=self.HEADERS)
        film = self.info(response.json()["docs"][0])

        return film

    def text_info(self, data: dict):

        message = (f"Имя: {data["name"]}\n"
                   f"Год: {data["year"]}\n"
                   f"Описание: {data["disc"]}\n")
        return message




if __name__ == "__main__":
    kinopoisk = KinopoiskApi()
    print(kinopoisk.search_films_name(name="Batman"))
