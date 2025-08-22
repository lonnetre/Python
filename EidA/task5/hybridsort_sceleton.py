import random


def hybrid_sort(arr, num_buckets):
    if len(arr) <= 1:
        return arr

    # Bucketsort
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])

    #Bucketsize
    bucket_size = (max(arr) - min(arr) + 1) / num_buckets
    for ele in arr:
        bucket_index = int((ele - min(arr)) // bucket_size)
        buckets[bucket_index].append(ele)

    # Rufe Mergesort auf
    res = []
    for bucket in buckets:
        sorted_bucket = merge_sort(bucket)
        res.extend(sorted_bucket)
        #for i in sorted_bucket:
        #    res.append(i)

    return res


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    middle = len(arr) // 2
    #from 0 ink, to middle exk.
    L = arr[:middle]
    #from middle ink, to len(arr) exk.
    R = arr[middle:]

    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)


def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1

    return merged


# Erstelle eine Liste mit 100 zufälligen Elementen zwischen 1 und 1000
arr = [random.randint(1, 1000) for _ in range(100)]
print("Unsortierte Liste: ", arr)

# Sortiere die Liste mittels Bucket Sort mit Mergesort als Unterprozess
sorted_arr = hybrid_sort(arr, 10)
print("Sortierte Liste: ", sorted_arr)
