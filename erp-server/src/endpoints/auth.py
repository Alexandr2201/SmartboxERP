from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import NoResultFound
from sqlalchemy import text
from validations.auth_validation import validate_username, validate_password
from logger import auth_logger as logger  # Используем логгер auth_service_logger

def create_auth_blueprint(Session):
    auth_bp = Blueprint('auth_bp', __name__)

    @auth_bp.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username', None)
        password = data.get('password', None)

        # Валидация логина и пароля
        valid, error_message = validate_username(username)
        if not valid:
            logger.error(error_message)
            return jsonify({"error": error_message}), 400

        valid, error_message = validate_password(password)
        if not valid:
            logger.error(error_message)
            return jsonify({"error": error_message}), 400
        
        # Проверка пользователя в базе данных
        session = Session()
        try:
            query = text("SELECT username FROM users WHERE username = :username AND convert_from(password, 'UTF8') = crypt(:password, convert_from(password, 'UTF8'));")
            user = session.execute(query, {'username': username, 'password': password}).fetchone()
            if user is None:
                logger.error("User not found")
                raise NoResultFound

            access_token = create_access_token(identity=username)
            logger.info(f'Logged in as: {username} ')

            return jsonify(access_token=access_token)
        except NoResultFound:
            logger.error("Bad username or password")
            return jsonify({"error": "Bad username or password"}), 401
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
        finally:
            session.close()

    @auth_bp.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        logger.debug(f'Checked user: {current_user}')
        return jsonify(logged_in_as=current_user), 200

    return auth_bp