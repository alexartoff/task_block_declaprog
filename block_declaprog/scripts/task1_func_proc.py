#!/usr/bin/env python


def odds_from_odds(lst): #func
    f1 = list(map(lambda item: list(filter(lambda i: item.index(i) % 2 == 0, item)), lst))
    return [item for indx, item in enumerate(f1) if indx % 2 == 0]


def keep_odds_from_odds(lst): #proc
    del lst[1::2]
    for indx, item in enumerate(lst):
        lst[indx] = item[::2]


def main():
    l = [[1, 2, 3], [4, 5, 6], [], [], [7, 8, 9]]
    ll = [
        [1, 2, 3, 4, 5],
        ['c', 'a', 't'],
        ['d', 'o', 'g'],
        [100, 200, 300, 400],
        [True, False],
        [],
        [],
    ]
    print('func', odds_from_odds(l))
    print('func', odds_from_odds([[1, 3], [], [7, 9]]))
    keep_odds_from_odds(l)
    print('proc', l)
    keep_odds_from_odds(l)
    print('proc', l)


if __name__ == "__main__":
    main()
