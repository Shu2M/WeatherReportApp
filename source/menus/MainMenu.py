"""Модуль определения главного меню приложения."""
from source.menus.Menu import Menu
from source.Option import Option
from source.commands.GoToWeatherReportMenuCommand import GoToCurveMenuCommand
from source.commands.NLastRecordsCommand import NLastRecordsCommand
from source.commands.BackMenuCommand import BackMenuCommand


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
                success_message='{result}',
            ),
            3: Option(
                name='Завершить работу приложения',
                command=BackMenuCommand(),
                success_message='',
            ),
        }
