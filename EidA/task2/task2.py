def bar(array, start, end):
    res = 1
    for i in range(start, end):
        res *= array[i]

    return res


def main():
    array = [1, 2, 3]
    print(bar(array, 0, len(array)))


if __name__ == '__main__':
    main()
