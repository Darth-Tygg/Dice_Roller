import random
import pyinputplus as pyip


class D2:
    def roll(self):
        d = random.randint(1, 2)
        return d


d_2 = D2()


class D4:
    def roll(self):
        d = random.randint(1, 4)
        return d


d_4 = D4()


class D6:
    def roll(self):
        d = random.randint(1, 6)
        return d


d_6 = D6()


class D8:
    def roll(self):
        d = random.randint(1, 8)
        return d


d_8 = D8()


class D10:
    def roll(self):
        d = random.randint(1, 10)
        return d


d_10 = D10()


class D12:
    def roll(self):
        d = random.randint(1, 12)
        return d


d_12 = D12()


class D20:
    def roll(self):
        d = random.randint(1, 20)
        return d


d_20 = D20()


class D100:
    def roll(self):
        d = random.randint(1, 100)
        return d


d_100 = D100()

x = 0

while x < 1:
    dice = pyip.inputNum("Which dice do you want to roll? Type either, 2, 4, 6, 8, 10, 12, 20, 100, or 0 to quit: ")
    x += 1
    if dice == 2:
        print(d_2.roll())

    elif dice == 4:
        print(d_4.roll())

    elif dice == 6:
        print(d_6.roll())

    elif dice == 8:
        print(d_8.roll())

    elif dice == 10:
        print(d_10.roll())

    elif dice == 12:
        print(d_12.roll())

    elif dice == 20:
        print(d_20.roll())

    elif dice == 100:
        print(d_100.roll())

    elif dice == 0:
        print('Goodbye')
        break

    x = 0
    continue
