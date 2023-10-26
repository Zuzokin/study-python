import time


class AutomaticWateringSystem:
    def __init__(self, initial_water_level, initial_soil_moisture):
        self.water_level = initial_water_level
        self.soil_moisture = initial_soil_moisture
        self.is_watering = False
        self.schedule = {}

    def start_watering(self, duration_minutes, water_amount):
        if self.water_level >= water_amount:
            self.water_level -= water_amount
            self.is_watering = True
            print(
                f"Начался полив на {duration_minutes} минут с использованием {water_amount} мл воды."
            )
            print("Полив завершен.")
        else:
            self.is_watering = False
            print("Недостаточно воды для полива.")

    def add_water(self, amount):
        self.water_level += amount
        self.log_message = (
            f"Добавлено {amount} мл воды. Текущий уровень воды: {self.water_level} мл."
        )

    def check_soil_moisture(self):
        return self.soil_moisture

    def check_water_level(self):
        return self.water_level

    def set_watering_schedule(self, start_time, duration_minutes, water_amount):
        # Установка расписания полива
        self.schedule = {
            "start_time": start_time,
            "duration_minutes": duration_minutes,
            "water_amount": water_amount,
        }
        print("Расписание полива установлено.")

    def run_scheduled_watering(self):
        # Проверка расписания и запуск полива при необходимости
        current_time = time.localtime()
        current_day = (
            current_time.tm_wday
        )  # Получаем текущий день недели (0 - Пн, 6 - Вс)

        if current_day in self.schedule:
            scheduled_info = self.schedule[current_day]
            start_time = scheduled_info["start_time"]
            duration_minutes = scheduled_info["duration_minutes"]
            water_amount = scheduled_info["water_amount"]

            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min
            scheduled_minute = start_time // 60
            scheduled_hour = start_time % 60

            if current_hour == scheduled_hour and current_minute >= scheduled_minute:
                print(f"Запуск запланированного полива на {duration_minutes} минут.")
                self.start_watering(duration_minutes, water_amount)
                return  # Добавляем return для выхода из метода после запуска полива


# Пример использования
if __name__ == "__main__":
    watering_system = AutomaticWateringSystem(
        initial_water_level=1000, initial_soil_moisture=50
    )

    watering_system.add_water(500)

    watering_system.set_watering_schedule(
        start_time=8 * 60, duration_minutes=10, water_amount=100
    )

    print(f"Влажность почвы: {watering_system.check_soil_moisture()}%")
    print(f"Уровень воды в резервуаре: {watering_system.check_water_level()} мл")

    watering_system.run_scheduled_watering()

    print(f"Влажность почвы: {watering_system.check_soil_moisture()}%")
    print(f"Уровень воды в резервуаре: {watering_system.check_water_level()} мл")
