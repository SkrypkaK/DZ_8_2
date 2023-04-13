import requests


# Функция делает попытку загрузить сайт Гугла и возвращает код ответа (код 200 = страница открывается успешно)
def try_google():
    r = requests.get("https://google.com")
    return r.status_code


def test_try_google():
    assert try_google() == 200
    print("OK!")


test_try_google()