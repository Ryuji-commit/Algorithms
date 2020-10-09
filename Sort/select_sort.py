import random


def select_max(unsorted, left, right):
    max_pos = left
    i = left
    while i <= right:
        if unsorted[i] > unsorted[max_pos]:
            max_pos = i
        i += 1

    return max_pos


def select_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n, 0, -1):
        max_pos = select_max(unsorted_list, 0, i - 1)
        if i - 1 != max_pos:
            unsorted_list[i-1], unsorted_list[max_pos] = unsorted_list[max_pos], unsorted_list[i-1]


if __name__ == "__main__":
    ListLength = 100
    my_list = [random.randint(0, 100) for _ in range(ListLength)]
    select_sort(my_list)
    print(my_list)
