def fizz_buzz(input_number: int) -> str or None:
    """
    This will test the input number and return the appropriate string
    1. If the number is divisible by 3, will return "fizz"
    2. If it's divisible by 5, will return "buzz".
    3. If it's divisible by both 3 and 5, will return "fizz buzz".
    4. If all of the above conditions are false, then it will return None
    :param input_number: The input number to be tested
    :return: "fizz"; "buzz"; "fizz buzz"; None
    """
    mod3 = input_number % 3
    mod5 = input_number % 5

    if (mod3 == 0) and (mod5 == 0):
        return "fizz buzz"
    elif mod3 == 0:
        return "fizz"
    elif mod5 == 0:
        return "buzz"
    else:
        return None


for i in range(101):
    result = fizz_buzz(i)
    if result:
        print("The number is {}, so {}".format(i, result))
