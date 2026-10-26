def calculateTestPassPerc(total_tests, passed_tests):
    if total_tests == 0:
        return 0

    percentage = (passed_tests/total_tests) * 100

    return percentage

print(calculateTestPassPerc(200, 120))

