"""Команда прогноза погоды по названию города."""
import types
import typing
import requests
from http import HTTPStatus
import datetime

from settings import WEATHER_DB
from settings import OPEN_WEATHER_API_KEY
from settings import OPEN_WEATHER_URL
from settings import ZERO_BY_KELVIN
from source.commands.Command import Command
from source.WeatherData import WeatherData


class WeatherReportByCityCommand(Command):
    """Команда прогноза погоды по названию города."""

    def execute(
        self,
        additional_data: typing.Any,
    ):
        """Метод исполнения команды.

        Args:
            additional_data: дополнительные данные (не требуются)

        Raises:
            ExitException: исключение выхода из цикла меню
        """
        weather_data = requests.get(
            OPEN_WEATHER_URL +
            "appid=" + OPEN_WEATHER_API_KEY +
            "&q=" + additional_data.city_name +
            "&lang=ru",
        ).json()

        result = RESPONSES_DISPATCH_DICT.get(
            int(weather_data['cod']),
            f'Мы не знаем, что произошло. Возможно, это ошибка '
            f'{weather_data["cod"]}: {weather_data["message"]}',
        )(weather_data)

        return True, result


def process_ok_response(weather_data: dict) -> WeatherData:
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
    return 'Не удалось получить прогноз. Возможно, вы неверно ' \
           'ввели название города. Попробуйте повторить запрос.'


RESPONSES_DISPATCH_DICT = types.MappingProxyType({
    HTTPStatus.OK: process_ok_response,
    HTTPStatus.NOT_FOUND: process_not_found_response,
})
