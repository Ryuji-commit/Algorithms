import random
import time


def insert(a, pos, value):
    i = pos - 1
    while i >= 0 and a[i] > value:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = value


def sort(a):
    for pos in range(1, len(a)):
        insert(a, pos, a[pos])


if __name__ == "__main__":
    ListLength = 500
    A = [random.randint(0, 500) for _ in range(ListLength)]
    print('List length : {}'.format(ListLength))
    print('before Insertion sort : {}'.format(A))
    start_time = time.time()
    sort(A)
    elapsed_time = time.time() - start_time
    print('sorted : {}'.format(A))
    print('elapsed time : {}sec'.format(elapsed_time))

