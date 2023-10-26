import time

import pytest


@pytest.mark.parametrize(
    "water_amount",
    [100, 200, pytest.param(1500, marks=pytest.mark.xfail())],
)
def test_start_watering_with_enough_water(
    watering_system_with_enough_water,
    water_amount,
):
    watering_system_with_enough_water.start_watering(
        duration_minutes=10, water_amount=water_amount
    )
    assert watering_system_with_enough_water.is_watering is True


# можно передать отрицательные значения
@pytest.mark.parametrize(
    "water_amount",
    [1500, pytest.param(-100, marks=pytest.mark.xfail())],
)
def test_start_watering_with_insufficient_water(
    watering_system_with_insufficient_water, water_amount
):
    watering_system_with_insufficient_water.start_watering(
        duration_minutes=10, water_amount=water_amount
    )
    assert watering_system_with_insufficient_water.is_watering is False


@pytest.mark.parametrize(
    "initial_water_level, initial_soil_moisture, amount, expected_water_level",
    [(1200, 50, 200, 1400)],
)
def test_add_water(
    create_watering_system_with_custom_parameters,
    initial_water_level,
    initial_soil_moisture,
    amount,
    expected_water_level,
):
    watering_system = create_watering_system_with_custom_parameters(
        initial_water_level=initial_water_level,
        initial_soil_moisture=initial_soil_moisture,
    )
    watering_system.add_water(amount=amount)
    assert watering_system.water_level == expected_water_level


@pytest.mark.parametrize(
    "initial_water_level, initial_soil_moisture, expected_soil_moisture",
    [(1200, 40, 40)],
)
def test_check_soil_moisture(
    create_watering_system_with_custom_parameters,
    initial_water_level,
    initial_soil_moisture,
    expected_soil_moisture,
):
    watering_system = create_watering_system_with_custom_parameters(
        initial_water_level=initial_water_level,
        initial_soil_moisture=initial_soil_moisture,
    )
    assert watering_system.soil_moisture == expected_soil_moisture


def test_set_watering_schedule(watering_system_with_schedule):
    assert watering_system_with_schedule.schedule == {
        "start_time": 720,
        "duration_minutes": 20,
        "water_amount": 150,
    }


@pytest.mark.parametrize(
    "current_time, expected_is_watering",
    [
        (time.struct_time((2023, 10, 26, 10, 30, 0, 3, 299, 0)), False),
        (time.struct_time((2023, 10, 25, 12, 0, 0, 2, 298, 0)), True),
    ],
)
def test_run_scheduled_watering(
    watering_system_with_schedule, mocker, current_time, expected_is_watering
):
    #    В функции run_scheduled_watering словарь self.schedule, auto_watering_system/auto_watering_system.py:41
    #    который мы инициализируем в set_watering_schedule не имеет ключа отвечающего за текущий день недели,
    #    и при это мы обращаемся к нему с проверкой if current_day in self.schedule
    #    auto_watering_system/auto_watering_system.py:51
    #    Проверка никогда не будет True и мы не будем получать значение is_watering is True
    mocker.patch("time.localtime", return_value=current_time)
    watering_system_with_schedule.run_scheduled_watering()
    assert watering_system_with_schedule.is_watering == expected_is_watering
