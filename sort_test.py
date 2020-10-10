from Sort import *
from random import randint
from copy import copy
from time import perf_counter


def main(unsorted_list):
    dict_of_sort_functions = dict(
        quick_sort=quick_sort.quick_sort,
        merge_sort=merge_sort.merge_sort_init,
        select_sort=select_sort.select_sort,
        bucket_sort=bucket_sort.bucket_sort,
        heap_sort=heap_sort.heap_sort,
        insertion_sort=insertion_sort.insertion_sort,
    )
    for sort_name, sort_function in dict_of_sort_functions.items():
        print(sort_name + ': {:.5f} sec'.format(handle_sort(unsorted_list, sort_function)))


def handle_sort(unsorted_list, sort_function):
    result = copy(unsorted_list)
    start_time = perf_counter()
    sort_function(result)
    elapsed_time = perf_counter() - start_time
    return elapsed_time


if __name__ == '__main__':
    random_list = [randint(0, 100) for _ in range(100)]
    main(random_list)
