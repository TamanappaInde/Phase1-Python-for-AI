def passwordStrengthCheck(password):
    if len(password) < 8:
        return "Weak Password"

    if not any(char.isdigit() for char in password):
        return "Password must contain a number."

    if not any(char.isupper() for char in password):
        return "Password must contain a upper case letter."

    return "Strong Password"

print(passwordStrengthCheck("mappa12"))
