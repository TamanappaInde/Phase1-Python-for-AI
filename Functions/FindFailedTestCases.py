def get_failed_testcases(test_results):
     failed_tests = []

     for test_name, status in test_results.items():
          if status == "Fail":
               failed_tests.append(test_name)

     return failed_tests;

results = {
     "Login Test": "Pass",
     "payment Test": "Pass",
     "Logout Test": "Fail",
     "Search Test": "Fail"
}

failed = get_failed_testcases(results)
print(failed)

