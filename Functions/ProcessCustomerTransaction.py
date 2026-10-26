def processTransaction(balance, amount):

    if amount <=0:
        return balance, "Invalid Transaction Amount"

    if amount > balance:
        return "Insufficient Balance"

    balance = balance - amount
    return balance, "Transaction Successfull"


balance, message = processTransaction(10000, 10000)

print(message)
print("Remaining Balance:", balance)

