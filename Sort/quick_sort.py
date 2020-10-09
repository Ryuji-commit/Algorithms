import random

TheStandardValueOfIFInsertion = 30


def insert(unsorted, pos, value, left_index):
    i = pos - 1
    while i >= left_index and unsorted[i] > value:
        unsorted[i+1] = unsorted[i]
        i -= 1
    unsorted[i+1] = value


def insertion_sort(unsorted, left_index, right_index):
    for pos in range(left_index + 1, right_index + 1):
        insert(unsorted, pos, unsorted[pos], left_index)


def select_pivot_index(left_index, right_index):
    return random.randint(left_index, right_index)


def partition(unsorted, left_index, right_index, pivot_index):
    counter = left_index
    unsorted[right_index], unsorted[pivot_index] = unsorted[pivot_index], unsorted[right_index]
    pivot_index = right_index
    pivot = unsorted[pivot_index]
    for i in range(left_index, right_index):
        if unsorted[i] <= pivot:
            unsorted[counter], unsorted[i] = unsorted[i], unsorted[counter]
            counter += 1
    unsorted[pivot_index], unsorted[counter] = unsorted[counter], unsorted[pivot_index]
    return counter


def quick_sort(unsorted_list, left_index, right_index):
    if left_index >= right_index:
        return
    pivot_index = select_pivot_index(left_index, right_index)
    pivot_index = partition(unsorted_list, left_index, right_index, pivot_index)

    if pivot_index-1-left_index <= TheStandardValueOfIFInsertion:
        insertion_sort(unsorted_list, left_index, pivot_index-1)
    else:
        quick_sort(unsorted_list, left_index, pivot_index-1)
    if right_index-pivot_index-1 <= TheStandardValueOfIFInsertion:
        insertion_sort(unsorted_list, pivot_index+1, right_index)
    else:
        quick_sort(unsorted_list, pivot_index+1, right_index)


if __name__ == "__main__":
    list_length = 100
    my_list = [random.randint(0, 100) for _ in range(list_length)]
    quick_sort(my_list, 0, list_length-1)
    print(my_list)


