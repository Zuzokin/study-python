# region Task 3
import pyscreenshot as ImageGrab
import time

import pyttsx3


def take_5_screenshots():
    while True:
        for i in range(5):
            # grab fullscreen
            im = ImageGrab.grab()

            # save image file
            im.save('screen' + str(i) + '.png')
            time.sleep(5)


# take_5_screenshots()

# endregion

# region Task 4
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print(fuzz.ratio("Я разобрался с виртуальным окружением", "Это оказалось совсем не трудно"))
print(fuzz.ratio("Я разобрался с виртуальным окружением!", "Я разобрался с виртуальным окружением!"))
print(fuzz.ratio("Я разобрался с виртуальным окружением?", "Я разобрался с виртуальным окружением!"))

# endregion

# region Task 5
# help('psutil')
import psutil
import pyttsx3

# help(psutil.sensors_battery)

battery = psutil.sensors_battery()


# battery_percentage = battery.percent


def say_warning(battery_percentage):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    if battery_percentage < 20:
        engine.say("Battery level is low")
        engine.runAndWait()


# say_warning(19)
# endregion

# region Task 6
# HH:MM
import re
from win11toast import toast
from datetime import datetime

alarm_time = "23:24"


def validate_time(alarm_time):
    if len(alarm_time) != 5:
        if re.fullmatch(r'\d\d:\d\d', alarm_time):
            hours, minutes = alarm_time.split(':')
            return int(hours) < 24 and int(minutes) < 60
    return False


def set_alarm():
    alarm_time = input('На какое время хотите поставить будильник?\nВведите время согласно шаблону HH:MM ->')
    if validate_time(alarm_time):
        print('Неверно указано время')
        return None
    hours, minutes = alarm_time.split(':')

    # title = input('Название будильника:')
    # message = input('Назначение:')
    title = '1'
    message = '2'
    # {'activationType': 'dismiss'}
    buttons = ['Остановить',
               'Отложить']
    alarm_sound = 'C:\Windows\Media\Alarm04.wav'
    # TODO доделать отложить
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    while True:
        if current_hour == int(hours) and current_min == int(minutes):
            toast(title,
                  message,
                  audio=alarm_sound,
                  buttons=buttons
                  )


# set_alarm()
# endregion

# region Task 7
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
API_KEY = os.getenv("API_KEY")

print(USERNAME, PASSWORD, API_KEY)
# endregion
