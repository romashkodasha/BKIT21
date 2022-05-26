
import json
import sys
from lab_python_fp.fieldm import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1

# Сделаем другие необходимые импорты
path = r"C:/Users/ASUS/PycharmProjects/LR3/data_light.json"


# Необходимо в переменную path сохранить путь к файлу, который был передан при
# запуске сценария
with open(path,'r') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise
# NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк
@print_result
def f1(arg):
    return sorted(list(Unique(field(arg,"job-name"))), key=str.lower)
    #return list(Unique(sorted(list(field(arg,'job-name')), key=str.lower)))
    #return list(Unique(field(arg,'job-name')))
@print_result
def f2(arg):
    return list(filter(lambda x: x.split()[0].lower() == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    out = list(zip(arg, list(gen_random(len(arg),100000,200000))))
    return list(map(lambda x: x[0] + ", зарплата " + str(x[1]) + " руб.",out))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))