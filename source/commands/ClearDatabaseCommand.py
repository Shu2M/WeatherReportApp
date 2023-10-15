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
        for record in WEATHER_DB.select(order_by='id'):
            WEATHER_DB.delete(record.id)
        return True, None
