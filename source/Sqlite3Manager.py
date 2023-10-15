"""Модуль определения класса работы с БД."""
import sqlite3


class Sqlite3Manager:
    """Класс для работы с БД sqlite3."""

    def __init__(self, database_filename: str) -> None:
        """Метод подключения к БД.

        Args:
            database_filename: имя БД
        """
        self.connection = sqlite3.connect(database_filename)

    def __del__(self):
        """Метод отключения от БД."""
        self.connection.close()

    def _execute(self, statement: str, values: list | tuple = None):
        """Метод выполнения команды SQL.

        Args:
            statement: инструкция sql
            values: значения для плейсхолдеров инструкций sql

        Returns:
            выполнивший инструкцию курсор из соединения с БД
        """
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name: str, columns: dict) -> None:
        """Метод создания таблицы.

        Если таблица БД была уже создана, ничего не делает

        Args:
            table_name: имя создаваемой таблицы БД
            columns: словарь с названиями колонок и их типами
        """
        columns_with_types = [
            f"{column_name} {column_type}"
            for column_name, column_type in columns.items()
        ]
        self._execute(
            f'''
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            '''
        )

    def add(self, table_name: str, data: dict) -> None:
        """Метод вставки в БД новых данных.

        Args:
            table_name: имя таблицы
            data: словарь, увязывающий имена и значения столбцов
        """
        placeholders = ', '.join('?' * len(data))
        column_names = ', '.join(data.keys())
        column_values = tuple(data.values())
        self._execute(
            f'''
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            ''',
            column_values
        )

    def delete(self, table_name: str, criteria: dict) -> None:
        """Метод удаления строки из таблицы БД.

        Args:
            table_name: имя таблицы
            criteria: словарь, увязывающий имена столбцов со значением на удаление
        """
        placeholders = [f'{column} = ?' for column in criteria.keys()]
        delete_criteria = ' AND '.join(placeholders)
        self._execute(
            f'''
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            ''',
            tuple(criteria.values())
        )

    def select(self, table_name: str, criteria: dict = None, order_by: str = None):
        """Метод отбора данных из таблицы SQL.

        Args:
            table_name: имя таблицы БД
            criteria: словарь критериев сортировки
            order_by: название столбца для сортировки результатов
        """
        criteria = criteria or {}
        query = f'SELECT * FROM {table_name}'

        if criteria:
            placeholders = [f'{column} = ?' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f' WHERE {select_criteria}'

        if order_by:
            query += f' ORDER BY {order_by}'

        return self._execute(
            query,
            tuple(criteria.values())
        )

    def update(self, table_name: str, criteria: dict, data: dict):
        """Метод обновления записи в выбранной строке.

        Args:
            table_name: имя таблицы
            criteria: критерии для обновления
            data: словарь данных для обновления
        """
        update_placeholders = [f'{column} = ?' for column in criteria.keys()]
        update_criteria = ' AND '.join(update_placeholders)

        data_placeholders = ', '.join(f'{key} = ?' for key in data.keys())

        values = tuple(data.values()) + tuple(criteria.values())

        self._execute(
            f'''
            UPDATE {table_name}
            SET {data_placeholders}
            WHERE {update_criteria};
            ''',
            values,
        )
