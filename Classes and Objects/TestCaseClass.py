class TestCase:
    def __init__(self, test_id, description, status):
        self.test_id = test_id
        self.description = description
        self.status = status

    def display_results(self):
        print("Test Case ID: ", self.test_id)
        print("Description: ", self.description)
        print("Status: ", self.status)

testcase1 = TestCase(
    "TC001",
    "Verify User Login",
    "Pass"
)

testcase1.display_results()

        