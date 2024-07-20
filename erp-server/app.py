from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from db.database import Session  # Изменен импорт
from endpoints.auth import create_auth_blueprint
from config import config_instance

#Для развертывания в продакшн рекомендуется использовать серверы,
#  такие как gunicorn или uwsgi в связке с обратным прокси-сервером, таким как Nginx.

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = config_instance.JWT_SECRET_KEY  # Секретный ключ для создания JWT

jwt = JWTManager(app)

# Создаем и регистрируем blueprint для аутентификации
auth_bp = create_auth_blueprint(Session)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
