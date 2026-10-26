def validateStatusCode(status_code):
    if status_code == 200:
        return "Request Successfull"
    elif status_code == 201:
        return "Data Created"
    elif status_code == 203:
        return "Request Processed"
    elif status_code == 204:
        return "Data not found"

    else:
        return "Invalid Status Code"
print(validateStatusCode(203))