userInput = input("Please enter 3 numbers separated by ',' :")
userInputArray = userInput.split(",")
userInputArray = [int(x) for x in userInputArray]
print(userInputArray[0] + userInputArray[1] - userInputArray[2])
