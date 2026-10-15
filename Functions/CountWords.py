def countWords(prompt):
    words = prompt.split()
    return len(words)
prompt = "Generate AI Test Cases"
print(countWords(prompt))

