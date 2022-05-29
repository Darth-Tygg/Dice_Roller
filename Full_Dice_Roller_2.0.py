import random
import pyinputplus as pyip

x = 0

while x < 1:
    dice = pyip.inputNum("Which dice do you want to roll? Type either, 2, 4, 6, 8, 10, 12, 20, 100, or 0 to quit: ")
    x += 1
    if dice == 2:
        print(random.randint(1, 2))

    elif dice == 4:
        print(random.randint(1, 4))

    elif dice == 6:
        print(random.randint(1, 6))

    elif dice == 8:
        print(random.randint(1, 8))

    elif dice == 10:
        print(random.randint(1, 10))

    elif dice == 12:
        print(random.randint(1, 12))

    elif dice == 20:
        print(random.randint(1, 20))

    elif dice == 100:
        print(random.randint(1, 100))

    elif dice == 0:
        print('Goodbye')
        break

    x = 0
    continue
