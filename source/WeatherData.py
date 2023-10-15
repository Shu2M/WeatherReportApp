"""Модуль датакласса данных о погоде."""
from dataclasses import dataclass


@dataclass
class WeatherData:
    """Датакласс данных погоды."""

    current_time: str = ''
    city_name: str = ''
    weather_conditions: str = ''
    current_temperature: int = 0
    perceived_temperature: int = 0
    wind_speed: int = 0

    def __str__(self):
        """Метод преобразования класса в строку."""
        return f'\n' \
               f'Текущее время: {self.current_time}\n' \
               f'Название города: {self.city_name}\n' \
               f'Погодные условия: {self.weather_conditions}\n' \
               f'Текущая температура: {self.current_temperature} °C\n' \
               f'Ощущается как: {self.perceived_temperature} °C\n' \
               f'Скорость ветра: {self.wind_speed} м/с\n'
