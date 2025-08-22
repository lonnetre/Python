import matplotlib.pyplot as plt
import time
import random


def lexi_sort(arr, pivot_func):
    lst = []
    for i in range(0, len(arr)):

        divisor = 1
        for j in range(0, len(str(arr[i])) - 1):
            divisor *= 10

        tmpLst = []
        for j in range(0, len(str(arr[i]))):
            x = arr[i] // divisor % 10
            tmpLst.append(x)
            divisor //= 10

        lst.append([arr[i], tmpLst])

    lst = quicksort(lst, pivot_func)

    sorted_lst = []
    for i, _ in lst:
        sorted_lst.append(i)

    return sorted_lst


def quicksort(arr, pivot_func):
    if len(arr) <= 1:
        return arr

    pivot_index = pivot_func(arr)
    pivot = arr[pivot_index]
    smaller, equal, larger = partition(arr, pivot)
    return quicksort(smaller, pivot_func) + equal + quicksort(larger, pivot_func)


def partition(arr, pivot):
    smaller = []
    equal = []
    larger = []

    for num, digits in arr:
        if compare_lexicographically(digits, pivot[1]):
            smaller.append([num, digits])
        elif compare_lexicographically(pivot[1], digits):
            larger.append([num, digits])
        else:
            equal.append([num, digits])
    return smaller, equal, larger


def compare_lexicographically(a, b):
    min_len = min(len(a), len(b))
    for i in range(min_len):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False
    return len(a) < len(b)


def num_to_list(x):
    lst = []

    divisor = 1
    for _ in range(0, len(str(x)) - 1):
        divisor *= 10

    for j in range(0, len(str(x))):
        res = x // divisor % 10
        lst.append(res)
        divisor //= 10

    return lst


def first_pivot(arr):
    return 0


def last_pivot(arr):
    return len(arr) - 1


def random_pivot(arr):
    return random.randint(0, len(arr) - 1)


def middle_pivot(arr):
    return len(arr) // 2


def median_first_middle_last_pivot(arr):
    first, middle, last = 0, len(arr) // 2, len(arr) - 1
    if compare_lexicographically(arr[first][1], arr[middle][1]) and compare_lexicographically(arr[middle][1],
                                                                                              arr[last][1]):
        return middle
    elif compare_lexicographically(arr[middle][1], arr[first][1]) and compare_lexicographically(arr[first][1],
                                                                                                arr[last][1]):
        return first
    elif compare_lexicographically(arr[first][1], arr[last][1]) and compare_lexicographically(arr[last][1],
                                                                                              arr[middle][1]):
        return last
    else:
        return first_pivot(arr)


def ninther_methode_pivot(arr):
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]

    if first <= middle <= last or last <= middle <= first:
        return len(arr) // 2
    elif middle <= first <= last or last <= first <= middle:
        return 0
    elif first <= last <= middle or middle <= last <= first:
        return len(arr) - 1
    else:
        return median_first_middle_last_pivot(arr)


def median_of_three(arr, a, b, c):
    if compare_lexicographically(arr[a][1], arr[b][1]) and compare_lexicographically(arr[b][1], arr[c][1]):
        return b
    elif compare_lexicographically(arr[b][1], arr[a][1]) and compare_lexicographically(arr[a][1], arr[c][1]):
        return a
    else:
        return c


def inefficient_pivot(arr):
    max_index = 0

    for i in range(1, len(arr)):
        if arr[max_index] < arr[i]:
            max_index = i

    return max_index


def measure_time(max_n, num_measurements):
    pivot_names = ['Erstes Pivot', 'Letztes Pivot', 'Zufälliges Pivot', 'Mittleres Pivot',
                   'Median Pivot', 'Ninther Pivot', 'Ineffizientes Pivot']
    pivot_colors = ['blue', 'red', 'green', 'cyan', 'yellow', 'magenta', 'black']
    pivot_times = [[0 for j in range(num_measurements)] for i in range(len(pivot_names))]
    iteration_problem_size = max_n // num_measurements
    current_problem_size = iteration_problem_size
    for i in range(num_measurements):
        arr = [random.randint(0, max_n) for i in range(current_problem_size)]
        current_problem_size += iteration_problem_size

        # Hier können Sie Elemente herausnehmen um nur bestimmte Methoden zu plotten
        for k, pivot in enumerate([first_pivot, last_pivot, random_pivot,
                                   middle_pivot, median_first_middle_last_pivot,
                                   ninther_methode_pivot,
                                   inefficient_pivot
                                   ]):
            t1 = time.time()
            lexi_sort(arr, pivot)
            t2 = time.time()
            pivot_times[k][i] = t2 - t1
    for k, pivot_name in enumerate(pivot_names):
        plt.scatter([], [], color=pivot_colors[k], label=pivot_name, alpha=0.5)
    for i in range(num_measurements):
        for k in range(len(pivot_names)):
            plt.scatter(i + 1, pivot_times[k][i], color=pivot_colors[k], alpha=0.5)

    plt.xlabel('Eingabegröße (n)')
    plt.ylabel('Sortierzeit (s)')
    plt.legend()
    plt.show()


# Beispieltests:
print(lexi_sort([], middle_pivot))
print(lexi_sort([1, 2, 3, ], middle_pivot))
print(lexi_sort([1, 2, 3, 11, 73, 1, 9, 38, 2, 14], middle_pivot))
print(lexi_sort([7, 11, 987], middle_pivot))
print(lexi_sort([3, 30, 34, 300, 345], middle_pivot))
# []
# [1, 2, 3]
# [1, 1, 11, 14, 2, 2, 3, 38, 73, 9]
# [11, 7, 987]

# Zeiten von Sortierung randomisierter Arrays vergleichen:
measure_time(1000, 10)
