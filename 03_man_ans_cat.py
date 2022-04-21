# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

class House:

    def __init__(self):
        self.food = 50
        self.dirt = 0

    def __str__(self):
        return 'Food in house {}, Dirt in house {}'.format(self.food, self.dirt)

class Human:

    def __init__(self):
        self.money = 100
        self.k = 1
        self.house = house
        self.fullness = 50

    def __str__(self):
        return "I'm human, my fulness {}, my money {}".format(self.fullness, self.money)



    def work(self):
        self.money += 50 * self.k
        cprint('Human work', color='blue')

    def promotion_on_work(self):
        self.k = 3
        cprint('Human has been promoted', color='blue')

    def buy_food(self):
        self.house.food += 50
        self.money -= 50
        cprint('Human bought food', color='blue')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('Human clean house', color='blue')

    def eat(self):
        self.fullness += 50
        self.house.food -= 30
        cprint('Human is eating', color='blue')

    def act(self):
        if self.fullness <= 0 or self.house.dirt >= 500:
            cprint('The human has dead {}', color='red')
            return
        elif self.house.food < 150 and self.money >= 50:
            self.buy_food()
        elif self.money <= 50:
            self.work()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.dirt > 100:
            self.clean_house()
        else:
            self.work()

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня
class Cat:

    def __init__(self, name):
        self.fullness = 20
        self.name = name
        self.house = None

    def pick_up_cat(self):
        self.house = house
        cprint('Human pick up a cat', color='green')

    def __str__(self):
        return "I'm {}, my fulness {}".format(self.name, self.fullness)

    def sleep(self):
        self.fullness -= 5
        cprint('{} slept'.format(self.name), color='yellow')

    def eat(self):
        self.fullness += 20
        self.house.food -= 10
        cprint('{} has ate'.format(self.name), color='yellow')

    def tear_up_a_wallpapers(self):
        self.fullness -= 20
        self.house.dirt += 5
        cprint('{} has teared up wallpapers'.format(self.name), color='yellow')

    def act(self):
        dice = randint(1, 2)
        if self.fullness < 0:
            cprint('{} has dead '.format(self.name), color='red')
            return
        elif self.fullness <= 20 and self.house.food >0:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.tear_up_a_wallpapers()

# Человеку и коту надо вместе прожить 365 дней.

house = House()
human = Human()
human.promotion_on_work()
names = [Cat(name='Mary'), Cat(name='Gosha'), Cat(name='Vasya'), Cat(name='Vadimidze'), Cat(name='Vitya'),
         Cat(name='Lena'), Cat(name='Dasha'), Cat(name='Olzhas')]
for cat in names:
    cat.pick_up_cat()
for day in range(1, 365):
    print('====================={}============================='.format(day))
    human.act()
    for cat in names:
        cat.act()
        cprint(cat, color='white')
    cprint(house, color='magenta')
    cprint(human, color='cyan')
    # cprint(cat, color='white')

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
