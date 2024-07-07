""""""
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import re
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Секретный ключ для создания JWT

jwt = JWTManager(app)

# Настройка подключения к PostgreSQL
DATABASE_URI = 'postgresql://postgres:A12345aa@localhost:5432/Smartbox SQL'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Имитация базы данных пользователей
#users_db = {
#    "admin": "A12345aa",
#    "user": "W12345ww"
#}

# Функция для валидации логина
def validate_username(username):
    if not 2 <= len(username) <= 255:
        return False
    # Простая проверка на SQL инъекции
    if re.search(r"[;'\"]", username):
        return False
    return True

# Функция для валидации пароля
def validate_password(password):
    if not 8 <= len(password) <= 255:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    return True

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

        # Валидация логина и пароля
    if not validate_username(username):
        return jsonify({"error": "Invalid username. Username must be between 2 and 255 characters and not contain any special characters."}), 400
    if not validate_password(password):
        return jsonify({"error": "Invalid password. Password must be between 8 and 255 characters long and contain both upper and lower case letters."}), 400

    # Проверка пользователя в базе данных
    session = Session()
    try:
        #query = text("SELECT username FROM users WHERE username = :username AND password = crypt(:password, password)")
        query = text("SELECT username FROM users WHERE username = :username AND convert_from(password, 'UTF8') = crypt(:password, convert_from(password, 'UTF8'));")
        user = session.execute(query, {'username': username, 'password': password}).fetchone()
        if user is None:
            raise NoResultFound

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    except NoResultFound:
        return jsonify({"error": "Bad username or password"}), 401
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    finally:
        session.close()

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run()
