"""Модуль определения подменю приложения для прогноза погоды."""
from source.menus.Menu import Menu
from source.Option import Option
from source.commands.WeatherReportByCityCommand import WeatherReportByCityCommand
from source.commands.WeatherReportByCoordinateCommand import WeatherReportByCoordinateCommand
from source.commands.BackMenuCommand import BackMenuCommand
from source.input_output_interface import get_parameterized_user_input_function


class WeatherReportMenu(Menu):
    """Класс подменю приложения."""

    def __init__(self):
        """Метод инициализации подменю приложения."""
        super().__init__()
        self.options = {
            1: Option(
                name='По городу',
                command=WeatherReportByCityCommand(),
                prep_call=get_parameterized_user_input_function(
                    city_name=('Введите название города', str)
                ),
                success_message='{result}',
            ),
            2: Option(
                name='По координате',
                command=WeatherReportByCoordinateCommand(),
                prep_call=get_parameterized_user_input_function(
                    lat=('Введите координату по широте', float),
                    lon=('Введите координату по долготе', float)
                ),
                success_message='{result}',
            ),
            3: Option(
                name='Вернуться в главное меню',
                command=BackMenuCommand(),
                success_message='',
            ),
        }
