"""Команда прогноза погоды по названию города."""
import typing

from source.commands.Command import Command
from source import exceptions


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
        return True, None
