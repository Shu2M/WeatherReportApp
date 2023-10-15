"""Команда очищения БД."""
import typing

from source.commands.Command import Command
from settings import WEATHER_DB


class ClearDatabaseCommand(Command):
    """Команда очищения БД."""

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
        for i in range(len(WEATHER_DB.select(order_by='id')), 0, -1):
            WEATHER_DB.delete(ind=i)
        return True, None
