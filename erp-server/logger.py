import logging
import os

# Создаем папку для хранения логов, если её нет
log_dir = './logs'
os.makedirs(log_dir, exist_ok=True)

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Создаем объект логгера
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

# Создаем файловый обработчик логов
log_file = os.path.join(log_dir, 'Auth_Service.log')
file_handler = logging.FileHandler(log_file)

# Форматируем сообщения логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)
