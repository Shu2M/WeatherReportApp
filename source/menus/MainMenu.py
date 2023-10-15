"""Модуль определения главного меню приложения."""
from source.menus.Menu import Menu
from source.Option import Option
from source.commands.GoToWeatherReportMenuCommand import GoToCurveMenuCommand
from source.commands.NLastRecordsCommand import NLastRecordsCommand
from source.commands.BackMenuCommand import BackMenuCommand
from source.commands.ClearDatabaseCommand import ClearDatabaseCommand
from source.input_output_interface import get_parameterized_user_input_function


class MainMenu(Menu):
    """Класс главного меню приложения."""

    def __init__(self):
        """Метод инициализации вида главного меню приложения."""
        super().__init__()
        self.options = {
            1: Option(
                name='Прогноз погоды',
                command=GoToCurveMenuCommand(),
                success_message='',
            ),
            2: Option(
                name='Просмотр последних записей',
                command=NLastRecordsCommand(),
                prep_call=get_parameterized_user_input_function(
                    n=('Введите количество записей, которые нужно вывести', int),
                ),
                success_message='{result}',
            ),
            3: Option(
                name='Очистить БД',
                command=ClearDatabaseCommand(),
                success_message='БД очищена',
            ),
            4: Option(
                name='Завершить работу приложения',
                command=BackMenuCommand(),
                success_message='',
            ),
        }
