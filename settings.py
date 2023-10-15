"""Модуль хранения настроечных констант."""
from pathlib import Path

from source.logger import get_logger


BASE_DIR_PATH = Path(__file__).resolve().parent

LOGGER_DIR_PATH = BASE_DIR_PATH
LOG_FILE_NAME = 'WeatherReportApp.log'
LOGGER_MODE = 'a'
FORMATTER_STRING = (
    '%(asctime)s - '
    '[%(levelname)s] - '
    '(%(funcName)s%(lineno)d) - '
    '%(message)s'
)
LOGGER = get_logger(
    filename=str(LOGGER_DIR_PATH / LOG_FILE_NAME),
    mode=LOGGER_MODE,
    formatter_string=FORMATTER_STRING,
)

WEATHER_DB_DIR_PATH = BASE_DIR_PATH
