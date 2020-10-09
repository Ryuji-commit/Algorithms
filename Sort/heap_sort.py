import random


def heapify(unsorted, idx, max_idx):
    largest = idx
    left_child = 2*idx + 1
    right_child = 2*idx + 2

    if left_child < max_idx and unsorted[left_child] > unsorted[largest]:
        largest = left_child
    if right_child < max_idx and unsorted[right_child] > unsorted[largest]:
        largest = right_child
    if largest != idx:
        unsorted[idx], unsorted[largest] = unsorted[largest], unsorted[idx]
        heapify(unsorted, largest, max_idx)


def build_heap(unsorted):
    len_of_a = len(unsorted)
    for i in range(len_of_a//2-1, -1, -1):
        heapify(unsorted, i, len_of_a)


def heap_sort(unsorted_list):
    len_of_a = len(unsorted_list)
    build_heap(unsorted_list)
    for i in range(len_of_a-1, 0, -1):
        unsorted_list[0], unsorted_list[i] = unsorted_list[i], unsorted_list[0]
        heapify(unsorted_list, 0, i)


if __name__ == "__main__":
    list_length = 100
    my_list = [random.randint(0, 100) for _ in range(list_length)]
    heap_sort(my_list)
    print(my_list)
