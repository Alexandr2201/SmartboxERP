import re

def validate_username(username):
    if not 2 <= len(username) <= 255:
        return False
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