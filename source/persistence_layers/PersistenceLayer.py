"""Модуль определения интерфейса слоя постоянства данных."""
from abc import ABC, abstractmethod


class PersistenceLayer(ABC):
    """Абстрактный класс слоя постоянства данных."""

    @abstractmethod
    def add(self, data: dict):
        """Метод добавления записи в ДБ.

        Args:
            data: словарь, увязывающий названия столбцов с их значениями
        """
        raise NotImplementedError('Слои постоянства данных должны реализовать метод create')

    @abstractmethod
    def select(self, criteria: dict = None, order_by: str = None):
        """Метод возврата списка строк из БД.

        Args:
            criteria: словарь критериев сортировки
            order_by: название столбца для сортировки результатов
        """
        raise NotImplementedError('Слои постоянства данных должны реализовать метод list')

    @abstractmethod
    def update(self, ind: int, data: dict):
        """Метод обновления записи в выбранной строке.

        Args:
            ind: номер строки
            data: словарь данных для обновления
        """
        raise NotImplementedError('Слои постоянства данных должны реализовать метод edit')

    @abstractmethod
    def delete(self, ind: int):
        """Метод удаления строки из таблицы БД.

        Args:
            ind: номер строки для удаления
        """
        raise NotImplementedError('Слои постоянства данных должны реализовать метод delete')
