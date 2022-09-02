# Task 1
import random


def random_num_gen():
    while True:
        a = random.randrange(100)
        yield a


# Task 2
func = float
lst = iter([1, 2, 3])


def map_gen(lst, func):
    while True:
        try:
            yield func(next(lst))
        except StopIteration:
            break


# Task 3

lst = [1, 2, 3]
def enum_gen(lst):
    lst = iter(lst)
    index = 0
    while True:
        try:
            yield index, next(lst)
            index +=1

        except StopIteration:
            break


# Task 4


lst = [1, 2, 3]
lst2 = [5, 6, 7]
def zip_gen(lst, lst2):
    lst = iter(lst)
    lst2 = iter(lst2)
    while True:
        try:
            yield next(lst), next(lst2)
        except StopIteration:
            break



