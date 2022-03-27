#!/usr/bin/env python


def non_empty_truths(lst):
    skip_list = [False, None, '', "", [], [0], 0]
    l1 = [[item for item in x if item not in skip_list] for x in lst if x not in skip_list]
    return [x for x in l1 if x not in skip_list]


def main():
    l = [[0, 1, 2], [], [], [0], [False, True, 42]]
    ll = [[0, ""], [False, None]]
    lll = [[0]]
    print(non_empty_truths(l))


if __name__ == "__main__":
    main()
