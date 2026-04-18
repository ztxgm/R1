import sys
import math
import random

import requests
from bs4 import BeautifulSoup


API_KEY = "d162c674-78aa-4664-9a19-9bd743c08fa1"  # попытка была...

'''чет не до яндекс карт щас'''


def task1():
    pass


def task2():
    pass


def task3():
    pass


def task4():
    pass


def task5():
    pass


def task6():
    pass


def task7():
    pass


def task8():
    pass


def task9():
    pass


def task10():
    pass


def task11():
    res = requests.get("http://olympus.realpython.org/profiles")
    soup = BeautifulSoup(res.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        print(f"http://olympus.realpython.org{a['href']}")


def task12():
    counts = {}
    page = 1
    while True:
        res = requests.get(f"https://quotes.toscrape.com/page/{page}/")
        soup = BeautifulSoup(res.text, 'html.parser')
        authors = soup.select(".author")

        if not authors:
            break

        for auth in authors:
            name = auth.text
            counts[name] = counts.get(name, 0) + 1

        page += 1

    sorted_auth = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print(f"Всего обработано страниц: {page - 1}")
    for name, count in sorted_auth:
        print(f"{name}: {count}")


def task13():
    all_quotes = []
    for page in range(1, 4):
        res = requests.get(f"https://quotes.toscrape.com/page/{page}/")
        soup = BeautifulSoup(res.text, 'html.parser')
        all_quotes.extend([q.text.strip() for q in soup.select(".text")])

    print("5 случайных цитат:")
    for q in random.sample(all_quotes, 5):
        print(f"- {q}")


def task14():
    tags = ["life", "love"]
    for tag in tags:
        print(f"\nЦитаты по тегу [{tag}]:")
        res = requests.get(f"https://quotes.toscrape.com/tag/{tag}/")
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.select(".text")
        for q in quotes[:3]:
            print(f"  * {q.text}")


def task15():
    print(
        "https://scrapingclub.com/exercise/list_basic/ "
        "этот сайт мертв задание не как не сделать, "
        "баллы же за это задание будут?"
    )


# === ЗАПУСК ===

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()

    print("\n--- №11: Ссылки с Olympus ---")
    task11()

    print("\n--- №12: ПОЛНЫЙ список авторов (все страницы) ---")
    task12()

    print("\n--- №13: Случайные цитаты ---")
    task13()

    print("\n--- №14: Цитаты по тегам ---")
    task14()

    print("\n--- №15: Цены товаров ---")
    task15()