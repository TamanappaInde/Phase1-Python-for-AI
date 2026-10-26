def loginValidation(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successfull."
    else:
        return "Invalid Credentials"

result = loginValidation("admin12", "admin123")
print(result)
