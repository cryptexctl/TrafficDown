"""
Пытался сократить код, из-за этого пишет дохуя "ошибок" с
неизвестными функциями, не переживайте, скрипт запускается без проблем!!
Почему не юзаю CustomTkinter, если система не винда: мне пишет ошибку на
андроиде, связанную с customtkinter да и похуй мне кажется мне лень
тестировать заново мб нет ошибки похуй мне лень тестировать
"""

import importlib.util
import os
import importlib


def no_gui():
    while True:
        for function in functions:

            print(f'{function["name"]} - {function["description"]}')

        choice = input("Введите название функции:\t")

        for function in functions:
            if function["name"] == choice.lower().strip():
                function["handler"]()


_os = "windows" if os.name == "nt" else "linux"
packages = ["requests", "tkinter", "threading", "customtkinter"]
for package in packages:
    if _os == "windows" and package == "tkinter":
        continue
    if _os == "linux" and package == "customtkinter":
        continue
    installed = importlib.util.find_spec(package)
    if not installed:

        os.system(f"python -m pip install {package}")

import requests  # noqa: E402 # type: ignore
import threading  # noqa: E402 # type: ignore

eat = False

urls = [
    "https://speedtest.rastrnet.ru/1GB.zip",
    "https://speedtest.rastrnet.ru/500MB.zip",
    "https://speedtest.selectel.ru/10GB",
    "https://speedtest.selectel.ru/1GB",
]  # большие файлы


def downloadThread(url):

    global eat, statuslbl, readed
    while eat:
        try:
            r = requests.get(url, stream=True, timeout=3)
            chunkSize = 5024000
            for chunk in r.iter_content(chunk_size=chunkSize):
                if not eat:
                    break
                # print(len(chunk))
                readed += len(chunk)
                text = f"Кушаем...\nПрочитано {round(readed/1024/1024, 1)} МБ"
                print(text)

                if useTkinter:
                    (
                        statuslbl.config(text=text)
                        if _os != "windows"
                        else statuslbl.configure(text=text)
                    )
        except requests.exceptions.ConnectionError:
            continue


def trafficDown():
    global eat
    if not useTkinter:
        print("Нажмите ENTER для остановки")
        input()
        eat = False
        return

    global statuslbl, readed

    eat = True
    readed = 0

    for url in urls:
        threading.Thread(target=downloadThread, args=(url,)).start()


functions = [
    {
        "name": "traffic",
        "description": "начать съедание трафика",
        "handler": trafficDown,
    },
    {
        "name": "exit",
        "description": "выход",
        "handler": lambda: os._exit(0),
    },
]


def startSpamTkinter():
    global eat
    if eat:
        startbtn.configure(text="Начать")
        statuslbl.configure(text="Тут будет статус")
        eat = False
    else:
        startbtn.configure(text="Остановить")
        eat = True
        trafficDown()


def checkWifi():
    try:
        requests.get("https://google.com")
        return True
    except requests.exceptions.ConnectionError:
        return False


while True:
    print("Проверяем доступ в интернет...")
    haveWifi = checkWifi()
    if haveWifi:
        break

if importlib.util.find_spec("tkinter"):
    useTkinter = True
else:
    useTkinter = False

try:
    if useTkinter and _os == "linux":
        from tk import window, startbtn, statuslbl

        startbtn.configure(command=startSpamTkinter)
        window.mainloop()
    elif useTkinter and _os == "windows":
        from custom_tk import window, startbtn, statuslbl

        startbtn.configure(command=startSpamTkinter)
        window.mainloop()
    else:
        print("Не удалось загрузить GUI. Используем терминальную версию.")
        no_gui()
except Exception as e:
    print(
        "Не удалось загрузить GUI. Используем терминальную версию.\nПричина:",
        e,
    )
    no_gui()
