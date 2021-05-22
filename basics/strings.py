print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include quotes" in strings')
print("hello" + " world")  # String concatenation
greeting = "Hello"
name = 'Bruce'
# if we want a space, we can add that too
print(greeting + " " + name)

splitString = "This string has been \nsplit over \nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh, ...he\'s resting".')

print("""The pet shop owner said "No, no, 'e's uh, ...he's resting". """)  # No need for escape characters

anotherSplitString = """This string has been 
split 
over 
several 
lines"""

print(anotherSplitString)

anotherSplitString = """This string has been \
split \
over \
several \
lines. But it is on the same line."""

print(anotherSplitString)

print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")  # r indicates raw string. Its better to use escape characters instead

age = 24
print(name + " is ", age, "years old")
print(type(age))

# number = "922,223;372:036 854,775;807"
number = "012,345;678:901"
print(number[3::4])

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
forwards = letters[::1]
print(backwards)
print(forwards)

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}"""
      .format(28, 30, 31))

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

# name = input("Please enter your name: ")
# print("Your name is ", name)
