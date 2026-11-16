# Todo doc and ANOTATION, достать постер / isibjnstance read
import requests



class KinopoiskApi:

    BASE_URL = "https://kinopoisk.dev/v1.5/movie"
    HEADERS = {"X-API-KEY": "FKV6CYW-22G42TA-Q7B1MNV-658FP78"}

    def random_film(self):
        url = "https://api.poiskkino.dev/v1.5/movie/random"
        response = requests.get(url=url, headers=self.HEADERS)
        film = self.info(data=response.json())
        print(film)
        message = self.text_info(data=film)
        return message


    def info(self, data):
        name = data.get("name", "Не найдено!")
        year = data.get("year", "Год не найден")
        disc = data.get("description", "Не найдено!")
        poster = data.get("poster", "Не найдено!")

        if isinstance(poster, dict):
            url = poster.get("url")
        else:
            url = poster

        film = {
            "name": name,
            "year": year,
            "disc": disc,
            "url": url,

        }
        return film


    def text_info(self, data: dict):

        message = (f"Имя: {data["name"]}\n"
                   f"Год: {data["year"]}\n"
                   f"Описание: {data["disc"]}\n"
                   f"Cсылка: {data['url']}")

        return message

    def search_film(self, name):
        url = f"https://api.poiskkino.dev/v1.5/movie/search?page=1&limit=10&query={name}"
        response = requests.get(url=url, headers=self.HEADERS)
        print(response.json())
        film = self.info(response.json()["docs"][0])
        message = self.text_info(data=film)
        return message


if __name__ == "__main__":
    kinopoisk = KinopoiskApi()
    print(kinopoisk.search_film(name="Batman"))
