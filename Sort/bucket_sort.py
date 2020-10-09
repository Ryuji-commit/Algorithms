import random


def insert(bucket, pos, value):
    i = pos - 1
    while i >= 0 and bucket[i] > value:
        bucket[i+1] = bucket[i]
        i -= 1
    bucket[i+1] = value


def insertion_sort(bucket):
    for pos in range(1, len(bucket)):
        insert(bucket, pos, bucket[pos])


def extract(buckets, unsorted):
    counter = 0
    for bucket in buckets:
        if len(bucket) == 0:
            continue

        if len(bucket) == 1:
            unsorted[counter] = bucket[0]
            counter += 1
        else:
            insertion_sort(bucket)
            for i in bucket:
                unsorted[counter] = i
                counter += 1


def bucket_hash(value):
    return value//3


def bucket_sort(unsorted_list):
    bucket_size = (max(unsorted_list)//3) + 1
    buckets = [[] for _ in range(bucket_size)]
    for i in unsorted_list:
        buckets[bucket_hash(i)].append(i)
    extract(buckets, unsorted_list)


if __name__ == "__main__":
    list_length = 100
    my_list = [random.randint(0, 100) for _ in range(list_length)]
    bucket_sort(my_list)
    print(my_list)
