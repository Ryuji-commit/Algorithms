import time
import random


def select_max(a, left, right):
    max_pos = left
    i = left
    while i <= right:
        if a[i] > a[max_pos]:
            max_pos = i
        i += 1

    return max_pos


def select_sort(a):
    n = len(a)
    for i in range(n, 0, -1):
        max_pos = select_max(a, 0, i - 1)
        if i - 1 != max_pos:
            a[i-1], a[max_pos] = a[max_pos], a[i-1]


if __name__ == "__main__":
    ListLength = 500
    A = [random.randint(0, 500) for _ in range(ListLength)]
    print('List length : {}'.format(ListLength))
    print('before Insertion sort : {}'.format(A))
    start_time = time.time()
    select_sort(A)
    elapsed_time = time.time() - start_time
    print('sorted : {}'.format(A))
    print('elapsed time : {}sec'.format(elapsed_time))
