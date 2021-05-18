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

name = input("Please enter your name: ")
print("Your name is ", name)
