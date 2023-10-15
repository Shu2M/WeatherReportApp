"""Команда показа N последних записей в БД."""
import typing

from source.commands.Command import Command
from source import exceptions


class NLastRecordsCommand(Command):
    """Команда показа N последних записей в БД."""

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
