# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:

    def __init__(self):
        self.name = 'WATER'

    def __str__(self):
        return 'WaTer'

    def __add__(self, other):
        if isinstance(other, Air().__class__):
            return "STORM"
        elif isinstance(other, Earth().__class__):
            return "DIRT"
        elif isinstance(other, Fire().__class__):
            return "STEAM"



class Fire:

    def __init__(self):
        self.name = 'FIRE'

    def __str__(self):
        return 'FIRE'

    def __add__(self, other):
        if isinstance(other, Air().__class__):
            return "LIGHTNING"
        if isinstance(other, Earth().__class__):
            return "LAVA"
        if isinstance(other, Water().__class__):
            return "STEAM"

class Earth:

    def __init__(self):
        self.name = 'EARTH'

    def __str__(self):
        return 'EARTH'

    def __add__(self, other):
        if isinstance(other, Air().__class__):
            return "DUST"
        if isinstance(other, Water().__class__):
            return "DIRT"
        if isinstance(other, Fire().__class__):
            return "LAVA"

class Air:

    def __init__(self):
        self.name = 'AIR'

    def __str__(self):
        return 'AIR'

    def __add__(self, other):
        if isinstance(other, Water().__class__):
            return "STORM"
        if isinstance(other, Earth().__class__):
            return "DUST"
        if isinstance(other, Fire().__class__):
            return "LIGHTNING"




water = Water()
air = Air()
# print(water+air)
# print(Water())
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

