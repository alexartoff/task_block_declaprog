#!/usr/bin/env python


from itertools import chain


def each2d(test, matrix):
    res = (True if test(x) else False for x in chain.from_iterable(matrix))
    for r in res:
        if not r:
            return False
    return True


def some2d(test, matrix):
    res = (True if test(x) else False for x in chain.from_iterable(matrix))
    for r in res:
        if r:
            return True
    return False


def sum2d(test, matrix):
    return sum(sum(item for item in elem if test(item)) for elem in matrix)


def is_int(x):
    return isinstance(x, int)


def each2d_t(test, matrix):
    return all(
        all(test(cell) for cell in row)
        for row in matrix
    )


def some2d_t(test, matrix):
    return any(
        any(test(cell) for cell in row)
        for row in matrix
    )


def main():
    print(each2d(is_int, [[1, 2], [3, 4]])) #True
    print(each2d(is_int, [[1, None], [3, 4]])) #False
    print(each2d(is_int, [])) #True
    # print(each2d(non_boom(is_positive), [[1, 2, 3], [4, 0, BOOM], [7, 8 ,9]])) #False
    print(some2d(is_int, [[None, "foo"], [(), {}]])) #False
    print(some2d(is_int, [[None, "foo"], [0, {}]])) #True
    print(some2d(is_int, [])) #False
    # print(some2d(non_boom(is_positive), [[1, -2, -3], [-4, 2, BOOM], [7, 8 ,9]])) #True
    print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]])) #111


if __name__ == "__main__":
    main()
