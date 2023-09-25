import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import json
import matplotlib.pyplot as plt
import numpy as np
from urllib.error import HTTPError
import folium
import nlpcloud

# region Task1
URL = "https://www.toybytoy.com/file/0028/8060.jpg"


def save_very_important_info(url):
    r = requests.get(url)
    r.raise_for_status()

    im = Image.open(BytesIO(r.content))
    im.save("very_important_info.jpg")


# save_very_important_info(URL)
# endregion


# region Task2
urls_list = [
    "https://www.toybytoy.com/file/0028/8060.jpg",
    "https://httpbin.org/status/404",
    "https://httpbin.org/get",
    "https://python-scripts.com/json",
    "https://habr.com/",
]


def check_urls_status(urls):
    for url in urls:
        try:
            r = requests.get(url)
            if r.status_code == requests.codes.ok:
                print(f"сайт {url} - доступен")
            else:
                print(f"сайт {url} - недоступен. Код ошибки - {r.status_code}")
        except requests.exceptions.RequestException as err:
            print(f"{url} не доступен. Ошибка при выполнении запроса: : {err}")


# check_urls_status(urls)
# endregion


# region Task3
def print_random_anime_quote():
    url = "https://waifu.it/api/quote"
    access_token = "NTA2MTg1ODM3Mzc4MDExMTU5.MTY5NDY4NzEyOQ--.8c8081aaf6"
    try:
        response = requests.get(
            url,
            headers={
                "Authorization": access_token,
            },
        )
        if response.status_code == requests.codes.ok:
            data = response.json()

            anime_name = data["anime"]
            author = data["author"]
            quote = data["quote"]

            print(f"Название аниме: {anime_name}")
            print(f"Автор: {author}")
            print(f"Цитата: {quote}")
        else:
            print(f"Код ошибки - {response.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: : {err}")


# print_random_anime_quote()
# endregion


# region Task4
def display_weather_info(city_name):
    url = "http://api.weatherapi.com/v1/current.json"
    api_key = "6f23a4b4bf284193aae120712231409"
    try:
        r = requests.get(
            url,
            params={
                "key": api_key,
                "q": city_name,
            },
        )
        if r.status_code == requests.codes.ok:
            weather_data = r.json()
            # weather_data_structure = json.dumps(weather_data, indent=2)
            # print(weather_data_structure)

            temperature = round(weather_data["current"]["temp_c"])
            temperature_feels = round(weather_data["current"]["feelslike_c"])
            clouds = weather_data["current"]["condition"]["text"]
            wind_speed = round(weather_data["current"]["wind_kph"] * 0.27)
            wind_dir = weather_data["current"]["wind_dir"]

            print(f"Сейчас в городе {city_name}: {temperature} градусов °C, {clouds}")
            print(f"Ощущается как {temperature_feels} градусов")
            print(f"Ветер: {wind_dir} {wind_speed} м/с")

        elif r.status_code == 400:
            error_data = r.json()
            print(f"Ой, что-то пошло не так!")
            print(f'Код ошибки: {error_data["error"]["code"]}')
            print(f'Описание:{error_data["error"]["message"]}')
        else:
            print(f"Код ошибки - {r.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: : {err}")


city = "Курск"
# display_weather_info(city)

# endregion


# region Task5
def convert_currency(amount=0, base_currency="RUB", target_currency="USD"):
    url = "https://api.freecurrencyapi.com/v1/latest"
    api_key = "fca_live_S3ndgq6ej2WOtOnOYisbpjHvTfEKlMe644RzKIXx"
    try:
        if amount < 0:
            raise ValueError("Amount must be greater than zero")

        r = requests.get(
            url,
            params={
                "apikey": api_key,
                "base_currency": base_currency,
                "currencies": target_currency,
            },
        )

        if r.status_code == requests.codes.ok:
            # data_structure = json.dumps(r.json(), indent=2)
            # print(data_structure)

            currency_data = r.json()
            exchange_rate = currency_data["data"][target_currency]
            convert_amount = amount * exchange_rate
            print(f"{amount} {base_currency} = {convert_amount} {target_currency}")

        elif r.status_code == 422:
            print(f"Указанные валюты не найдены, код ошибки: {r.status_code}")
        else:
            print(f"Код ошибки: {r.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: : {err}")
    except ValueError as val_err:
        print(val_err)


# convert_currency(1, "USD", "RUB")
# endregion


# region Task6
def visualize_temp_per_days(city_name="Курск", num_days=14):
    daily_weather_data = daily_weather_forecast(city_name, num_days)

    days = np.arange(1, num_days + 1)
    temp = [day["day"]["avgtemp_c"] for day in daily_weather_data]

    plt.title(f"Изменение температуры в городе {city} за последние {num_days} дней")
    plt.xlabel("Дата")
    plt.ylabel("Градусов цельсия")
    plt.grid(which="major", linestyle=":", linewidth="1", color="black")

    dates = [day["date"].split("-")[2] for day in daily_weather_data]
    plt.xticks(ticks=days, labels=dates)

    plt.plot(
        days,
        temp,
        marker="o",
        markerfacecolor="tab:red",
    )

    plt.show()


def daily_weather_forecast(city_name="Курск", days=7):
    url = "http://api.weatherapi.com/v1/forecast.json"
    api_key = "6f23a4b4bf284193aae120712231409"
    try:
        r = requests.get(
            url,
            params={
                "key": api_key,
                "q": city_name,
                "days": days,
            },
        )
        if r.status_code == requests.codes.ok:
            weather_data = r.json()

            # weather_data_structure = json.dumps(weather_data, indent=2)
            # print(weather_data_structure)

            # for x in weather_data["forecast"]["forecastday"]:
            #     print(x)

            return weather_data["forecast"]["forecastday"]

        elif r.status_code == 400:
            error_data = r.json()
            print("Ой, что-то пошло не так!")
            print(f'Код ошибки: {error_data["error"]["code"]}')
            print(f'Описание:{error_data["error"]["message"]}')
        else:
            print(f"Код ошибки - {r.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: : {err}")


# visualize_temp_per_days()


# endregion


# region Task7
def save_earth_photos():
    # api_key = "j8BlxWgz2RQ9lGH46wkuPBRxfcxpU4vHdNcGfUYh"
    date = "2022-07-07"

    date_url = "https://epic.gsfc.nasa.gov/api/natural/date/" + date
    convert_date = date.replace("-", "/")
    url_to_get_photo = f"https://epic.gsfc.nasa.gov/archive/natural/{convert_date}/png/"

    try:
        # отправляю запрос, чтобы получить данные о фотографиях
        response = requests.get(date_url)
        if response.status_code != 200:
            raise HTTPError

        photos_data = response.json()
        if not photos_data:
            raise ValueError("Не удалось загрузить данные")
    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: {err}")
        return None
    except HTTPError:
        print(f"Ошибка http: {response.status_code}")
        return None
    except ValueError as val_err:
        print(f"Данные о фотографиях отсутствуют. Ошибка - {val_err}")
        return None

    # Список для хранения id фотографий
    photos_ids = []
    for photo in photos_data:
        photos_ids.append(photo["image"])

    # Список для хранения кадров
    frames = []
    for photo_id in photos_ids:
        try:
            # Открываем изображение каждого кадра. PS работает не очень быстро, тк фотографии высокого качества
            frame = Image.open(
                requests.get(url_to_get_photo + photo_id + ".png", stream=True).raw
            )
            # Добавляем кадр в список с кадрами.
            frames.append(frame)

        except UnidentifiedImageError as err:
            print(f"Ошибка при скачивании изображения {photo_id}: {err}")

    if not frames:
        print("Не удалось скачать фотографии")
        return None

    # Берем первый кадр и в него добавляем оставшееся кадры.
    frames[0].save(
        "Earth.gif",
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=100,
        loop=0,
    )


# save_earth_photos()
# endregion


# region Task8
def find_by_ip(ip):
    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url + ip)
        if response.status_code != 200:
            raise HTTPError
        data = response.json()
        coords = data["lat"], data["lon"]

        m = folium.Map(location=coords, zoom_start=12)

        folium.Marker(
            location=coords,
            tooltip="Попался",
            popup="Вор тут",
            icon=folium.Icon(color="red"),
        ).add_to(m)

        m.save("map.html")

    except requests.exceptions.RequestException as err:
        print(f"Ошибка при выполнении запроса: {err}")
    except HTTPError as e:
        print(f"Ошибка http - {e}: код http - {response.status_code}")


# find_by_ip("115.41.218.39")
# endregion


# region Task9
def generate_image_by_description(description):
    token = "086f7046a96a544aef7c1e5e9697b421a81412e5"

    client = nlpcloud.Client(
        "stable-diffusion",
        token,
        gpu=True,
        lang="rus_Cyrl",
    )

    image_link = client.image_generation(description)
    print(image_link)


description = """Битва Таноса и Винни-Пуха"""
# generate_image_by_description(description)
# endregion
