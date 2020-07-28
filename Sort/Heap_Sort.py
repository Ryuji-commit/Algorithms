import random
import time


def heapify(a, idx, max_idx):
    largest = idx
    left_child = 2*idx + 1
    right_child = 2*idx + 2

    if left_child < max_idx and a[left_child] > a[largest]:
        largest = left_child
    if right_child < max_idx and a[right_child] > a[largest]:
        largest = right_child
    if largest != idx:
        a[idx], a[largest] = a[largest], a[idx]
        heapify(a, largest, max_idx)


def build_heap(a):
    len_of_a = len(a)
    for i in range(len_of_a//2-1, -1, -1):
        heapify(a, i, len_of_a)


def heap_sort(a):
    len_of_a = len(a)
    build_heap(a)
    for i in range(len_of_a-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i)


if __name__ == "__main__":
    ListLength = 1000
    A = [random.randint(0, 500) for _ in range(ListLength)]
    print('List length : {}'.format(ListLength))
    print('before Heap sort : {}'.format(A))
    start_time = time.time()
    heap_sort(A)
    elapsed_time = time.time() - start_time
    print('sorted : {}'.format(A))
    print('elapsed time : {}sec'.format(elapsed_time))
