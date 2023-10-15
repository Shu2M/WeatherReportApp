"""Команда прогноза погоды по текущему местоположению пользователя."""
import typing
import requests
import geocoder

from settings import OPEN_WEATHER_API_KEY
from settings import OPEN_WEATHER_URL
from source.commands.Command import Command
from source.http_cod_process import RESPONSES_DISPATCH_DICT, process_unknown_response


class WeatherReportByCurrentLocationCommand(Command):
    """Команда прогноза погоды по текущему местоположению пользователя."""

    def execute(
        self,
        additional_data: typing.Any,
    ):
        """Метод исполнения команды.

        Args:
            additional_data: дополнительные данные (не требуются)

        Returns:
            статус, результат работы команды
        """
        weather_data = requests.get(
            OPEN_WEATHER_URL +
            "appid=" + OPEN_WEATHER_API_KEY +
            "&q=" + geocoder.ip('me').city +
            "&lang=ru",
        ).json()

        result = RESPONSES_DISPATCH_DICT.get(
            int(weather_data['cod']),
            process_unknown_response,
        )(weather_data)

        return True, result
