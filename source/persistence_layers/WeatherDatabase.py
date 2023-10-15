"""Реализация слоя постоянства данных для хранения записей о погоде."""
from source.persistence_layers.PersistenceLayer import PersistenceLayer
from source.Sqlite3Manager import Sqlite3Manager
from source.WeatherData import WeatherData


class WeatherDatabase(PersistenceLayer):
    """Класс слоя постоянства данных прогнозов погоды."""

    def __init__(self, table_name: str, table_path: str):
        """Метод инициализации таблицы БД о прогнозах погоды.

        Если такой БД еще не существует, то создает новую согласно
        указанным в настройках параметрам

        Args:
            table_name: название таблицы БД
            table_path: путь до файла БД
        """
        self.table_name = table_name
        self.db = Sqlite3Manager(table_path)

        self.db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'current_time': 'text not null',
            'city_name': 'text not null',
            'weather_conditions': 'text not null',
            'current_temperature': 'integer',
            'perceived_temperature': 'integer',
            'wind_speed': 'integer',
        })

    def add(self, weather_data: dict):
        """Метод добавления записи прогноза погоды в ДБ.

        Args:
            weather_data: словарь, увязывающий названия столбцов с их значениями
        """
        self.db.add(self.table_name, weather_data)

    def select(self, criteria: dict = None, order_by: str = None) -> list[WeatherData]:
        """Метод возврата списка прогноза погоды из БД.

        Args:
            criteria: словарь критериев сортировки
            order_by: название столбца для сортировки результатов

        Returns:
            список с объектами WeatherData
        """
        selected_records = []
        for record in self.db.select(
                self.table_name,
                criteria=criteria,
                order_by=order_by
        ).fetchall():
            selected_records.append(WeatherData(*record[1:]))
        return selected_records

    def update(self, ind, weather_data):
        """Метод обновления записи прогноза в выбранной строке.

        Args:
            ind: номер строки
            weather_data: словарь данных для обновления
        """
        self.db.update(self.table_name, {'id': ind}, weather_data)

    def delete(self, ind):
        """Метод удаления строки из таблицы БД.

        Args:
            ind: номер строки для удаления
        """
        self.db.delete(self.table_name, {'id': ind})