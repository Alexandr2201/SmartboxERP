from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import NoResultFound
from sqlalchemy import text
import re

def create_auth_blueprint(Session):
    auth_bp = Blueprint('auth_bp', __name__)

    def validate_username(username):
        if not 2 <= len(username) <= 255:
            return False
        # Простая проверка на SQL инъекции
        if re.search(r"[;'\"]", username):
            return False
        return True

    def validate_password(password):
        if not 8 <= len(password) <= 255:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        return True

    @auth_bp.route('/login', methods=['POST'])
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

    @auth_bp.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

    return auth_bp