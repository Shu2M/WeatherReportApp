"""Команда показа N последних записей в БД."""
import typing

from source.commands.Command import Command
from settings import WEATHER_DB


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
        if additional_data.n <= 0:
            return True, 'Недопустимое вводимое значение. ' \
                         'Требуется ввести число больше нуля'

        all_records = WEATHER_DB.select(order_by='id')

        if not all_records:
            result = 'Записи отсутствуют'
        elif len(all_records) < additional_data.n:
            result = 'Введенное число превышает количество записей в БД, ' \
                     'поэтому будут выведены все результаты\n\n'
            for record in all_records:
                result += str(record)
        else:
            result = all_records[-additional_data.n:]

        return True, result
