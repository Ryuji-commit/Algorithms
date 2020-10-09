import random


def insert(unsorted, pos, value):
    i = pos - 1
    while i >= 0 and unsorted[i] > value:
        unsorted[i+1] = unsorted[i]
        i -= 1
    unsorted[i+1] = value


def insertion_sort(unsorted_list):
    for pos in range(1, len(unsorted_list)):
        insert(unsorted_list, pos, unsorted_list[pos])


if __name__ == "__main__":
    ListLength = 100
    my_list = [random.randint(0, 100) for _ in range(ListLength)]
    insertion_sort(my_list)
    print(my_list)

