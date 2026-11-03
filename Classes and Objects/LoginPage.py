class LoginPage:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print("Entering Username: ", self.username)
        print("Entering Password: ", self.password)
        print("Clicking on login button")

user1 = LoginPage(
    "testuser", "test123"
)

user1.login()


        