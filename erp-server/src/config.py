import json
import os

class Config:
    def __init__(self, config_file='server.config.json'):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

    @property
    def JWT_SECRET_KEY(self):
        return self.config.get('jwt_secret_key')

    @property
    def DATABASE_URI(self):
        db_config = self.config.get('database', {})
        db_print = f"postgresql://{db_config.get('user')}:{db_config.get('password')}@" \
               f"{db_config.get('host')}:{db_config.get('port')}/{db_config.get('dbname')}"
        print(db_print)
        return f"postgresql://{db_config.get('user')}:{db_config.get('password')}@" \
               f"{db_config.get('host')}:{db_config.get('port')}/{db_config.get('dbname')}"

    @property
    def LOG_LEVEL(self):
        return self.config.get('log_level', 'INFO').upper()

# Инициализация конфигурации
config_instance = Config()