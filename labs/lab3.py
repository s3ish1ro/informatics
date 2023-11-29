import random
import string


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

task1()
