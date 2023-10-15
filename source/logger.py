"""Модуль настройки логгера."""
import logging


def get_logger(filename: str, mode: str, formatter_string: str):
    """Функция создания и настройки режимов работы и вывода логгера.

    Args:
        filename: путь хранения лог файла
        mode: режим записи логов
        formatter_string: шаблон записи логов

    Returns:
        настроенный объект логгера
    """
    logger = logging.getLogger()
    file_handler = logging.FileHandler(
        filename=filename,
        mode=mode,
    )
    formatter = logging.Formatter(formatter_string)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger
