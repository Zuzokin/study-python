# region Task1
import requests


def check_status():
    URL = input('Введите URL-адрес веб-страницы')

    r = requests.get(URL)
    status = r.status_code
    if r.status_code == requests.codes.ok:
        print(f'Успешно, код состояния: {status}')
    else:
        print(f'Не успешно, код состояния: {status}')


# check_status()

# endregion

# region Task2
from PIL import Image

picture = 'cat.jpg'


def change_image(pic):
    im = Image.open(pic)
    print(im.format, im.size, im.mode)
    out = im.resize((128, 128))
    print(out.format, out.size, out.mode)
    out.save("new_image.jpg")
    im.close()
    out.close()


# change_image(picture)
# endregion

# region Task3
from pytube import YouTube

link = 'https://www.youtube.com/watch?v=xOe5kBeJQEM'
wrong_link = 'https://www.youtube.com/watch?v=xOe5kB123eJQEM'


def download_video(_link):
    try:
        yt_video = YouTube(_link)
    except:
        print("Connection Error")
    try:
        (yt_video.streams
         .filter(file_extension='mp4')
         .first()
         .download()
         )
    except:
        print('При скачивании произошла ошибка')
    else:
        print('Видео успешно загружено')


# download_video(link)
# endregion

# region Task4
from colorama import Fore, Back, Style


def bring_some_colors_to_this_gray_world():
    print(Fore.GREEN + 'some green text')
    print(Fore.BLACK + Back.WHITE + 'and with a WHITE background')
    print(Style.RESET_ALL)
    print('back to normal now')
    print(Fore.CYAN + Back.MAGENTA + 'and colorful with a GREEN background')
    print(Style.RESET_ALL)


# endregion

# region Task5
import emoji

line = 'Buy 📈📈📈 the programming after 👀 school 👏📚🏫 course! 😂'
print(emoji.demojize(line))
# endregion

# region Task6
import pyperclip, time


def convert_clipboard_string():
    while True:
        text = pyperclip.waitForNewPaste()
        text = ' '.join(text.split()).lower().replace('ё', 'е')
        pyperclip.copy(text)
        time.sleep(1)


# convert_clipboard_string()
# endregion

# region Task7
import wikipedia as wiki

print(wiki.summary('Computer program'))

# endregion
