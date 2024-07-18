import logging
import os

# Функция для создания и настройки логгера
def setup_logger(logger_name, log_file, level=logging.INFO):
    log_dir = './logs'
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Создаем файловый обработчик логов
    log_file = os.path.join(log_dir, log_file)
    file_handler = logging.FileHandler(log_file)

    # Форматируем сообщения логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger

# Создание логгеров для разных сервисов
auth_logger = setup_logger('auth_service_logger', 'Auth_Service1.log')
# Можно создать другие логгеры для других сервисов, например:
# user_logger = setup_logger('user_service_logger', 'User_Service.log')
