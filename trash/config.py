class Config:
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    DATABASE_URI = 'postgresql://postgres:A12345aa@localhost:5432/Smartbox SQL'

def create_app():
    import connexion
    from flask_cors import CORS
    from flask_jwt_extended import JWTManager

    # Создаем приложение Connexion
    app = connexion.App(__name__, specification_dir='./')
    app.add_api('authService.yaml')

    flask_app = app.app
    flask_app.config.from_object(Config)

    # Настраиваем CORS и JWT
    CORS(flask_app)
    jwt = JWTManager(flask_app)

    return flask_app