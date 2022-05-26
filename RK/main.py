# используется для сортировки
from operator import itemgetter
from data import*

def task1():
    task_1=[]
    for i in range(len(one_to_many)):
        if ((one_to_many[i][2])[0] == 'A'):
            task_1.append(one_to_many[i])
    return task_1
def task2():
    res_2_unsorted = []
    # Перебираем все среды программирования
    for t in tools:
        # Список языков сред программирования
        t_lang = list(filter(lambda x: x[2] == t.name, one_to_many))
        # Если среда программирования не пуста
        if len(t_lang) > 0:
            res_2_unsorted.append((t.name, max(t_lang, key=lambda x: x[1])[1]))

    # Сортировка по новизне
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    return(res_2)
def task3():
    res_3 = []
    # Перебираем все среды программирования
    for lang, _, tool in many_to_many:
        res_3.append((lang, tool))
    res_3 = sorted(res_3, key=itemgetter(1))
    return(res_3)

def main():

    print('Задание Г1')
    print(task1())
    print('\nЗадание Г2')
    print(task2())
    print('\nЗадание Г3')
    print(task3())


if __name__ == '__main__':
    main()

