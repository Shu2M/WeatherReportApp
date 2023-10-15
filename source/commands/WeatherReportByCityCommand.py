"""Команда прогноза погоды по названию города."""
import typing
import requests

from settings import OPEN_WEATHER_API_KEY
from settings import OPEN_WEATHER_URL
from source.commands.Command import Command
from source.http_cod_process import RESPONSES_DISPATCH_DICT, process_unknown_response


class WeatherReportByCityCommand(Command):
    """Команда прогноза погоды по названию города."""

    def execute(
        self,
        additional_data: typing.Any,
    ):
        """Метод исполнения команды.

        Args:
            additional_data: дополнительные данные city_name

        Returns:
            статус, результат работы команды
        """
        weather_data = requests.get(
            OPEN_WEATHER_URL +
            "appid=" + OPEN_WEATHER_API_KEY +
            "&q=" + additional_data.city_name +
            "&lang=ru",
        ).json()

        result = RESPONSES_DISPATCH_DICT.get(
            int(weather_data['cod']),
            process_unknown_response,
        )(weather_data)

        return True, result
