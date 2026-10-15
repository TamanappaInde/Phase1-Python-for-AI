def validatePrompt(prompt):
    if prompt.strip() == "":
        return "Prompt can not be empty"
    return "Valid Prompt"
print(validatePrompt("generate test cases"))

