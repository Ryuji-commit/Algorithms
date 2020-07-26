import random
import time


def insert(a, pos, value):
    counter = 1
    i = pos - 1
    while i >= 0 and a[i] > value:
        a[i+1] = a[i]
        i -= 1
        counter += 1
    a[i+1] = value
    return counter


def sort(a):
    process_counter = 0
    for pos in range(1, len(a)):
        process_counter += insert(a, pos, a[pos])

    return process_counter


if __name__ == "__main__":
    ListLength = 500
    A = [random.randint(0, 500) for _ in range(ListLength)]
    print('List length : {}'.format(ListLength))
    print('before Insertion sort : {}'.format(A))
    start_time = time.time()
    process_number = sort(A)
    elapsed_time = time.time() - start_time
    print('sorted : {}'.format(A))
    print('process count : {}'.format(process_number))
    print('elapsed time : {}sec'.format(elapsed_time))

