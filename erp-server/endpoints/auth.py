from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import NoResultFound
from sqlalchemy import text
from validations.auth_validation import validate_username, validate_password
from logger import logger

def create_auth_blueprint(Session):
    auth_bp = Blueprint('auth_bp', __name__)

    @auth_bp.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username', None)
        password = data.get('password', None)

        # Валидация логина и пароля
        if not validate_username(username):
            logger.error("Invalid username. Username must be between 2 and 255 characters and not contain any special characters")
            return jsonify({"error": "Invalid username. Username must be between 2 and 255 characters and not contain any special characters."}), 400
        if not validate_password(password):
            logger.error("Invalid password. Password must be between 8 and 255 characters long and contain both upper and lower case letters")
            return jsonify({"error": "Invalid password. Password must be between 8 and 255 characters long and contain both upper and lower case letters."}), 400

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
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
        finally:
            session.close()

    @auth_bp.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        logger.info(f'Checked user: {current_user}')
        return jsonify(logged_in_as=current_user), 200

    return auth_bp