def testresult(expected, actual):
    if expected == actual:
        return "Pass"
    else:
        return "Fail"
print(testresult(250,200))

