import re

def validate_username(username):
    if not 2 <= len(username) <= 255:
        return False, "Invalid username. Username must be between 2 and 255 characters"
    if re.search(r"[;'\"]", username):
        return False, "Invalid username. Username must not contain any special characters"
    return True, ""

def validate_password(password):
    if not 8 <= len(password) <= 255:
        return False, "Invalid password. Password must be between 8 and 255 characters long"
    if not re.search(r"[a-z]", password):
        return False, "Invalid password. Password must contain at least one lowercase letter"
    if not re.search(r"[A-Z]", password):
        return False, "Invalid password. Password must contain at least one uppercase letter"
    return True, ""