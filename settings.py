"""Модуль хранения настроечных констант."""
from pathlib import Path

from source.logger import get_logger
from source.persistence_layers.WeatherDatabase import WeatherDatabase


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
WEATHER_DB_NAME = 'weather_reports'
WEATHER_DB = WeatherDatabase(
    table_name=WEATHER_DB_NAME,
    table_path=str(BASE_DIR_PATH / f'{WEATHER_DB_NAME}.db'),
)
