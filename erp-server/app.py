import connexion
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from db.database import Session
from endpoints.auth import auth_bp

# Создаем приложение Connexion
app = connexion.App(__name__, specification_dir='./specifications/')
app.add_api('authService.yaml')

# Получаем Flask приложение из Connexion
flask_app = app.app

CORS(flask_app)
flask_app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

jwt = JWTManager(flask_app)

if __name__ == '__main__':
    app.run(port=5000)