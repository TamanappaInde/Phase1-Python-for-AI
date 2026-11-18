with open("employee.txt", "r") as file:
    data = file.read()

print("Employee Details: ")
print(data)

# Read a file line by line
print("Read a file line by line")
with open("employee.txt", "r") as file:
    for line in file:
        print(line.strip())


# Read all lines in to list
with open("employee.txt", "r") as file:
    lines = file.readlines()

print(lines)
# Count the lines
print("Total Lines: ", len(lines))
