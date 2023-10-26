import pytest

from auto_watering_system.auto_watering_system import AutomaticWateringSystem


@pytest.fixture()
def watering_system_with_enough_water():
    return AutomaticWateringSystem(initial_water_level=1000, initial_soil_moisture=50)


@pytest.fixture()
def watering_system_with_insufficient_water():
    return AutomaticWateringSystem(initial_water_level=0, initial_soil_moisture=50)


@pytest.fixture()
def create_watering_system_with_custom_parameters():
    def custom_watering_system(initial_water_level, initial_soil_moisture):
        return AutomaticWateringSystem(initial_water_level, initial_soil_moisture)

    return custom_watering_system


@pytest.fixture()
def watering_system_with_schedule(watering_system_with_enough_water):
    watering_system_with_enough_water.set_watering_schedule(
        start_time=720, duration_minutes=20, water_amount=150
    )
    return watering_system_with_enough_water


# class MockTime:
#
#     @staticmethod
#     def localtime():
#         return time.struct_time(
#             (
#             tm_year=2023,
#             tm_mon=10,
#             tm_mday=26,
#             tm_hour=10,
#             tm_min=30,
#             tm_sec=0,
#             tm_wday=3,
#             tm_yday=299,
#             tm_isdst=0,
#         )
#         )
#
#
# @pytest.fixture()
# def mock_localtime(monkeypatch):
#     def mock_get(*args, **kwargs):
#         return MockTime()
#
#     monkeypatch.setattr(time, "localtime", mock_get)
