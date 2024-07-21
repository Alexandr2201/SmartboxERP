import logging
import os
from config import config_instance

# Функция для создания и настройки логгера
def setup_logger(logger_name, log_file, level=logging.INFO):
    # Создаем папку для хранения логов, если её нет
    log_dir = './logs'
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Создаем файловый обработчик логов
    log_file_path = os.path.join(log_dir, log_file)
    file_handler = logging.FileHandler(log_file_path)

    # Форматируем сообщения логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger

# Преобразование уровня логирования из строки в соответствующий уровень
log_level = getattr(logging, config_instance.LOG_LEVEL.upper(), logging.INFO)
# Создание логгеров для разных сервисов
auth_logger = setup_logger('auth_service_logger', 'Auth_Service.log', level=log_level)
# Можно создать другие логгеры для других сервисов, например:
# user_logger = setup_logger('user_service_logger', 'User_Service.log')
