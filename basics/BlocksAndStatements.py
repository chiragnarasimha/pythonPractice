# # Challenge 1
# # Using if with strings
#
# tree1 = "pine"
# # tree2 = "coconut"
# tree2 = "pine"
#
# if tree1 == tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different")
#
# # Challenge 2: Simple condition
# x = 5
# y = 7
# if x == y:
#     print("x equals y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is smaller than y")
#
# age = int(input("How old are you? "))
#
# # if age >= 16 and age <= 65:
# # if 16 <= age <= 65:
# if age in range(16, 66):
#     print("Have a good day at work")
# else:
#     print("Enjoy your free time")
#
# print("-" * 80)
#
# if age < 16 or age > 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
#

# # Challenge: Extracting capitals
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# capitals = ""
# for char in quote:
#     if char.isupper():
#         capitals += char
#         print(char)
#
# print(capitals)
#
# for i in range(0, 10):
#     print(i)

# for i in range(0, 100):
#     if (i % 7) == 0:
#         print(i)
#
# for i in range(0, 100, 7):
#     print(i)
#     if ((i % 11) == 0) and (i is not 0):
#         break

# for i in range(0, 20):
#     if (i % 3 == 0) or (i % 5 == 0):
#         continue
#     else:
#         print(i)

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(0, multiplier):
    answer += number

print(answer)
