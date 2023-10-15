"""Команда прогноза погоды по координате."""
import typing

from source.commands.Command import Command
from source import exceptions


class WeatherReportByCoordinateCommand(Command):
    """Команда прогноза погоды по координате."""

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
        return True, None
