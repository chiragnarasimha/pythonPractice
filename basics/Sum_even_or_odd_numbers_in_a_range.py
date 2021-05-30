def sum_eo(n: int, t: str):
    if t == "e":
        return sumNumbers(0, n)
    elif t == "o":
        return sumNumbers(1, n)
    else:
        return -1


def sumNumbers(start: int, end: int):
    sum_temp = 0
    for i in range(start, end, 2):
        sum_temp += i
    return sum_temp


print(sum_eo(10, "e"))
print(sum_eo(7, "o"))
