# -*- coding: utf-8 -*-
from random import randrange

import simple_draw as sd
sd.resolution = (1200, 900)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, number):
        self.number = number
        self.x = randrange(100, 1200, 30)
        self.y = randrange(0, 900, 30)
        self.fallen_flakes = 0

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=100, color=sd.COLOR_WHITE)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=100, color=sd.background_color)

    def move(self):
        self.y -= 10

    def get_fallen_flakes(self):
        if self.y <= 0:
            self.fallen_flakes += 1

    def flakeupper(self):
        if self.y < 0:
            self.y += 900

    def __del__(self):
        print('number=', self.number,'cycles=', self.fallen_flakes)


def get_flakes (count):
    global flakes
    flakes = []
    for N in range(count):
        # flake = Snowflake
        flakes.append(Snowflake(N))


#
# for _ in range(10):
#     # flake.points()
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     # if not flake.can_fall():
#     #     break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
N = 10
get_flakes(count=N)
fallen = 0

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.get_fallen_flakes()  # подчитать сколько снежинок уже упало
        if flake.y <= 0:
            fallen += 1
        flake.flakeupper()
        print(fallen)
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break



sd.pause()
