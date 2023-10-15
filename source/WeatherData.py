"""Модуль датакласса данных о погоде."""
from dataclasses import dataclass
import datetime


@dataclass
class WeatherData:
    """Датакласс данных погоды."""

    id: int = 0
    current_time: datetime.datetime = ''
    city_name: str = ''
    weather_conditions: str = ''
    current_temperature: int = 0
    perceived_temperature: int = 0
    wind_speed: int = 0

    def __str__(self):
        """Метод преобразования класса в строку.

        Returns:
            отформатированную строку прогноза погоды
        """
        return f'\n' \
               f'Время прогноза: {self.current_time}\n' \
               f'Название города: {self.city_name}\n' \
               f'Погодные условия: {self.weather_conditions}\n' \
               f'Текущая температура: {self.current_temperature} °C\n' \
               f'Ощущается как: {self.perceived_temperature} °C\n' \
               f'Скорость ветра: {self.wind_speed} м/с\n'

    def __iter__(self):
        """Метод итератора."""
        yield 'current_time', self.current_time
        yield 'city_name', self.city_name
        yield 'weather_conditions', self.weather_conditions
        yield 'current_temperature', self.current_temperature
        yield 'perceived_temperature', self.perceived_temperature
        yield 'wind_speed', self.wind_speed
