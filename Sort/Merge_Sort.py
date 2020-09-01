import random
import time


def merge_sort_init(a):
    copy = list(a)
    merge_sort(copy, a, 0, len(a))


def merge_sort(a, result, start, end):
    if end - start < 2:
        return

    if end - start == 2:
        if result[start] > result[start+1]:
            result[start], result[start+1] = result[start+1], result[start]
        return

    mid = (start + end)//2
    merge_sort(result, a, start, mid)
    merge_sort(result, a, mid, end)

    i = start
    j = mid
    idx = start
    while idx < end:
        if j >= end or (i < mid and a[i] < a[j]):
            result[idx] = a[i]
            i += 1
        else:
            result[idx] = a[j]
            j += 1

        idx += 1


if __name__ == "__main__":
    ListLength = 500
    A = [random.randint(0, 500) for _ in range(ListLength)]
    print('List length : {}'.format(ListLength))
    print('before Merge sort : {}'.format(A))
    start_time = time.time()
    merge_sort_init(A)
    elapsed_time = time.time() - start_time
    print('sorted : {}'.format(A))
    print('elapsed time : {}sec'.format(elapsed_time))