import random
import time

TheStandardValueOfIFInsertion = 30


def insert(a, pos, value, left_index):
    i = pos - 1
    while i >= left_index and a[i] > value:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = value


def insertion_sort(a, left_index, right_index):
    for pos in range(left_index, right_index + 1):
        insert(a, pos, a[pos], left_index)


def select_pivot_index(left_index, right_index):
    return random.randint(left_index, right_index)


def partition(a, left_index, right_index, pivot_index):
    counter = left_index
    a[right_index], a[pivot_index] = a[pivot_index], a[right_index]
    pivot_index = right_index
    pivot = a[pivot_index]
    for i in range(left_index, right_index):
        if a[i] <= pivot:
            a[counter], a[i] = a[i], a[counter]
            counter += 1
    a[pivot_index], a[counter] = a[counter], a[pivot_index]
    return counter


def quick_sort(a, left_index, right_index):
    if left_index >= right_index:
        return
    pivot_index = select_pivot_index(left_index, right_index)
    pivot_index = partition(a, left_index, right_index, pivot_index)

    if pivot_index-1-left_index <= TheStandardValueOfIFInsertion:
        insertion_sort(a, left_index, pivot_index-1)
    else:
        quick_sort(a, left_index, pivot_index-1)
    if right_index-pivot_index-1 <= TheStandardValueOfIFInsertion:
        insertion_sort(a, pivot_index+1, right_index)
    else:
        quick_sort(a, pivot_index+1, right_index)


if __name__ == "__main__":
    ListLength = 500
    A = [random.randint(0, 500) for _ in range(ListLength)]
    print('List length : {}'.format(ListLength))
    print('before Insertion sort : {}'.format(A))
    start_time = time.time()
    quick_sort(A, 0, ListLength-1)
    elapsed_time = time.time() - start_time
    print('sorted : {}'.format(A))
    print('elapsed time : {}sec'.format(elapsed_time))


