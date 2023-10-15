"""Модуль функций обработки ошибок."""
import types
from http import HTTPStatus
import datetime

from settings import WEATHER_DB
from settings import ZERO_BY_KELVIN
from source.WeatherData import WeatherData


def process_ok_response(weather_data: dict) -> WeatherData:
    """Функция обработки ответа 200.

    Args:
        weather_data: данные, полученные по запросу request

    Returns:
        объект WeatherData
    """
    weather_report = WeatherData(
        current_time=str(datetime.datetime.now()),
        city_name=weather_data['name'],
        weather_conditions=weather_data['weather'][0]['description'],
        current_temperature=round(weather_data['main']['temp'] - ZERO_BY_KELVIN),
        perceived_temperature=round(weather_data['main']['feels_like'] - ZERO_BY_KELVIN),
        wind_speed=round(weather_data['wind']['speed']),
    )
    WEATHER_DB.add(weather_data=weather_report)
    return weather_report


def process_not_found_response(weather_data: dict) -> str:
    """Функция обработки 404 ошибки.

    Args:
        weather_data: данные, полученные по запросу request (не требуется)

    Returns:
        строку с ответом
    """
    return 'Не удалось получить прогноз. Возможно, вы неверно ' \
           'ввели название города. Попробуйте повторить запрос.'


def process_unknown_response(weather_data: dict) -> str:
    """Функция обработки неизвестной ошибки.

        Args:
            weather_data: данные, полученные по запросу request

        Returns:
            строку с ответом
        """
    return f'Мы не знаем, что произошло. Возможно, это ошибка ' \
           f'{weather_data["cod"]}: {weather_data["message"]}'


RESPONSES_DISPATCH_DICT = types.MappingProxyType({
    HTTPStatus.OK: process_ok_response,
    HTTPStatus.NOT_FOUND: process_not_found_response,
})