class BaseTest:
    def setUp(self):
        print("Opening Browser")

class LoginTest(BaseTest):
    def login_test(self):
        print("Testing Login Functionality")

test = LoginTest()

test.setUp()
test.login_test()

