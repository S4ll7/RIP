#!/usr/bin/env python3
import json
from librip.ex5 import timer
from librip.ex4 import print_result
from librip.ex1 import field, gen_random
from librip.ex2 import Unique

# path = "data_light_cp1251.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open("data_light_cp1251.json") as read_file:
    data = json.load(read_file)


@print_result
def f1(arg):
    return list(Unique(list(field(arg, "job-name")), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda s: "программист" in s, arg))


@print_result
def f3(arg):  # map(func, arr)
    return list(map(lambda s: s + " с опытом Python", arg))


@print_result
def f4(arg):
    prof = gen_random(100000, 200000, len(arg))
    return list(map(lambda s: '{}, зарплата {} руб.'.format(s[0], s[1]), zip(arg, prof)))


with timer():
    f4(f3(f2(f1(data))))
1
Downloading1
