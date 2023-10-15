"""Модуль определения подменю приложения для прогноза погоды."""
from source.menus.Menu import Menu
from source.Option import Option
from source.commands.WeatherReportByCityCommand import WeatherReportByCityCommand
from source.commands.WeatherReportByCoordinateCommand import WeatherReportByCoordinateCommand
from source.commands.BackMenuCommand import BackMenuCommand


class WeatherReportMenu(Menu):
    """Класс подменю приложения."""

    def __init__(self):
        """Метод инициализации подменю приложения."""
        super().__init__()
        self.options = {
            1: Option(
                name='По городу',
                command=WeatherReportByCityCommand(),
                success_message='{result}',
            ),
            2: Option(
                name='По координате',
                command=WeatherReportByCoordinateCommand(),
                success_message='{result}',
            ),
            3: Option(
                name='Вернуться в главное меню',
                command=BackMenuCommand(),
                success_message='',
            ),
        }
