from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from db.database import Session  # Изменен импорт
from endpoints.auth import create_auth_blueprint

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Секретный ключ для создания JWT

jwt = JWTManager(app)

# Создаем и регистрируем blueprint для аутентификации
auth_bp = create_auth_blueprint(Session)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
