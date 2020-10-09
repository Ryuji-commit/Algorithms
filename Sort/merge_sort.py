import random


def merge_sort_init(unsorted_list):
    copy = list(unsorted_list)
    merge_sort(copy, unsorted_list, 0, len(unsorted_list))


def merge_sort(unsorted, result, start, end):
    if end - start < 2:
        return

    if end - start == 2:
        if result[start] > result[start+1]:
            result[start], result[start+1] = result[start+1], result[start]
        return

    mid = (start + end)//2
    merge_sort(result, unsorted, start, mid)
    merge_sort(result, unsorted, mid, end)

    i = start
    j = mid
    idx = start
    while idx < end:
        if j >= end or (i < mid and unsorted[i] < unsorted[j]):
            result[idx] = unsorted[i]
            i += 1
        else:
            result[idx] = unsorted[j]
            j += 1

        idx += 1


if __name__ == "__main__":
    list_length = 100
    my_list = [random.randint(0, 100) for _ in range(list_length)]
    merge_sort_init(my_list)
    print(my_list)
