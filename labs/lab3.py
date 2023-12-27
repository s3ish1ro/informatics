import random
import string
import os


def print_char_list(array):
    print(*array)


def task1():
    def create_random_array(n):
        array = []
        a = string.ascii_letters + string.digits
        for i in range(n):
            array.append(random.choice(a))
        return array
    digits = string.digits
    array = create_random_array(10)
    ans = []
    for element in array:
        for digit in digits:
            if element == digit:
                element = "*"
        ans.append(element)
    print_char_list(array)
    print_char_list(ans)


def task2():
    def print_char_2d_array(array):
        for i in range(len(array)):
            print(*array[i])

    a = ('*', '.')
    random_array = [[random.choice(a) for _ in range(5)] for _ in range(5)]
    print_char_2d_array(random_array)


def task3():
    for _ in range(5):
        word = str(input('Введите слово '))
        if word[0] not in '0123456789':
            with open(word[0] + "-words.dat", 'a') as file:
                file.write(word + '\n')


def task4():
    def print_string_list(array):
        for i in range(len(array)):
            print(array[i])

    def get_string_array_from_console(n):
        console_array = []
        for i in range(n):
            console_array.append(str(input('Введите математический термин в ед. числе ')))
        return console_array

    def proverka(array1, array2):
        for i in range(len(array1)):
            if array1[i] in array2:
                array1[i] += ' ✓'
        return array1

    math_termins = ('Вектор', 'Предел', 'Интеграл', 'Производная', 'График функции', 'Матрица',
                    'Определитель', 'Тригонометрическая функция', 'Гиперболическая функция', 'Асимптота',
                    'Точка экстремума', 'Точка перегиба')

    user_array = proverka(get_string_array_from_console(len(math_termins)), math_termins)
    print_string_list(user_array)


def task5():
    with open('task5.txt', 'a') as file:
        print('Введите текст ')
        while True:
            text = str(input())
            file.write(text + '\n')


def task6():
    with open('variant5.txt', 'r') as file:
        info = ''
        for _ in range(10):
            info += file.readline()
        stats = (file.readline().split())
        node, epto1, epto2, epto3 ,eptoint, eptoeqv = [], [], [], [], [], []
        file_array = [x for x in file]
        for i in range(len(file_array)):
            node_i, epto1_i, epto2_i, epto3_i, eptoint_i, eptoeqv_i = file_array[i].split()
            node.append(node_i)
            epto1.append(epto1_i)
            epto2.append(epto2_i)
            epto3.append(epto3_i)
            eptoint.append(eptoint_i)
            eptoeqv.append(eptoeqv_i)

        array = (node, epto1, epto2, epto3, eptoint, eptoeqv)
        for i in range(len(array)):
            file = open(f'{stats[i]}.dat', 'w')
            for el in array[i]:
                (file.write(el + '\n'))


def task7():
    with open('task7.txt', 'r') as file:
        file_array = [x for x in file.readlines()]
        array = []
        paths = []
        for i in range(len(file_array)):
            array.append(file_array[i].rstrip().split('\\'))
        for i in range(len(array)):
            path = ''
            for j in range(len(array[i]) - 1):
                path += array[i][j] + '\\'
            if not os.path.isdir(path):
                os.makedirs(path)
            paths.append(path)
        for i in range(len(paths)):
            if '.' in array[i][-1]:
                _ = open(paths[i] + array[i][-1], 'w')
            else:
                os.mkdir(paths[i] + array[i][-1])


