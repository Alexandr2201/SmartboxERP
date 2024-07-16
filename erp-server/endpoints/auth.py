from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager  # Добавлен импорт JWTManager
from sqlalchemy.exc import NoResultFound
from sqlalchemy import text
from db.database import Session
from validations.auth_validations import validate_username, validate_password
from logger import logger  # Импортируем logger из logger.py
import jwt
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    logger.info("Some information")
    logger.error("An error occurred")
    
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

    if not validate_username(username):
        return jsonify({"error": "Invalid username. Username must be between 2 and 255 characters and not contain any special characters."}), 400
    if not validate_password(password):
        return jsonify({"error": "Invalid password. Password must be between 8 and 255 characters long and contain both upper and lower case letters."}), 400

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
    auth_header = request.headers.get('Authorization')
    logger.info(f"Authorization Header: {auth_header}")

    if not auth_header or 'Bearer ' not in auth_header:
        logger.error("No authorization token provided.")
        return jsonify({"error": "Нет предоставленного токена авторизации"}), 401

    token = auth_header.split('Bearer ')[1].strip()

    try:
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
    except jwt.ExpiredSignatureError:
        logger.error("Token expired.")
        return jsonify({"error": "Токен истек"}), 401
    except jwt.InvalidTokenError:
        logger.error("Invalid token.")
        return jsonify({"error": "Неверный токен"}), 401
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
