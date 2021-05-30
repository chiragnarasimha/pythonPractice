menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))

print("---------")
# Delete items from then end of the list, so that index of the list
# items do now change during the run
for meal in menu:
    meal_length = len(meal) - 1  # This is because the array index will start at 0
    for index, meal_item in enumerate(reversed(meal)):
        if meal_item == "spam":
            del meal[meal_length - index]
    print(meal)

print("---------")
# Another way to iterate backwards in a list
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for i in range(len(meal) - 1, -1, -1):
        if meal[i] == "spam":
            del meal[i]

    print(meal)
