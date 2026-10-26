def generate_login_testcases(requirement):

    test_cases = [
        {
            "id": "TC001",
            "scenario": "Login with valid username and password",
            "expected": "Login should be successful"
        },
        {
            "id": "TC002",
            "scenario": "Login with invalid password",
            "expected": "Error message should be displayed"
        },
        {
            "id": "TC003",
            "scenario": "Login with empty credentials",
            "expected": "Validation message should be displayed"
        }
    ]

    return {
        "requirement": requirement,
        "test_cases": test_cases
    }

requirement = "User should be able to login using valid credentials"

results = generate_login_testcases(requirement)

for test_case in results["test_cases"]:
    print(test_case)

    