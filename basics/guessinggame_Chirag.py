import random

aveCount = 0

numberOfTimesToRun = 100
forCounter = 0

for i in range(0, numberOfTimesToRun):
    highest = 1000
    lowest = 1
    answer = random.randint(1, highest)
    count = 0
    guess = 0  # initialise to any number that doesn't equal the answer

    while guess != answer:
        count += 1
        guess = (highest + lowest) // 2
        # print("Guess is {}".format(guess))
        if guess == 0:
            break
        if guess == answer:
            # print("It took {0} iterations to guess the answer ->> {1}".format(count, guess))
            break
        else:
            if guess < answer:
                # print("Guessed {}. Guess is too low".format(guess))
                lowest = guess - 1  # To make the code run more efficiently
            else:  # guess must be greater than answer
                # print("Guessed {}. Guess is too high".format(guess))
                highest = guess + 1
    aveCount += count
    forCounter += 1

print("It took an average of {} to guess the correct answer".format(aveCount / numberOfTimesToRun))
print(forCounter)
print(aveCount)
