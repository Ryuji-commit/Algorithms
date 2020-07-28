import random
import time


def insert(bucket, pos, value):
    i = pos - 1
    while i >= 0 and bucket[i] > value:
        bucket[i+1] = bucket[i]
        i -= 1
    bucket[i+1] = value


def insertion_sort(bucket):
    for pos in range(1, len(bucket)):
        insert(bucket, pos, bucket[pos])


def extract(buckets, a):
    counter = 0
    for bucket in buckets:
        if len(bucket) == 0:
            continue

        if len(bucket) == 1:
            a[counter] = bucket[0]
            counter += 1
        else:
            insertion_sort(bucket)
            for i in bucket:
                a[counter] = i
                counter += 1


def bucket_hash(value):
    return value//3


def bucket_sort(a):
    buckets = [[] for _ in range(len(a))]
    for i in a:
        buckets[bucket_hash(i)].append(i)
    extract(buckets, a)


if __name__ == "__main__":
    ListLength = 500
    A = [random.randint(0, 500) for _ in range(ListLength)]
    print('List length : {}'.format(ListLength))
    print('before Bucket sort : {}'.format(A))
    start_time = time.time()
    bucket_sort(A)
    elapsed_time = time.time() - start_time
    print('sorted : {}'.format(A))
    print('elapsed time : {}sec'.format(elapsed_time))
