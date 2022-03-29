#!/usr/bin/env python


def my_map(func, itr):
    for x in itr:
        yield func(x)


def my_filter(func, itr):
    for x in itr:
        if func(x):
            yield x


def replicate_each(n, itr):
    for x in itr:
        # yield from (x for _ in range(n))
        for _ in range(n):
            yield x


def main():
    print(list(my_map(abs, [-1, 2, -3]))) #[1, 2, 3]
    print(list(my_filter(lambda x: x % 2 == 1, range(10))))
    print(list(replicate_each(2, [1, 'a']))) #[1, 1, 'a', 'a']
    print(list(replicate_each(0, [1, 'a']))) #[]


if __name__ == "__main__":
    main()
