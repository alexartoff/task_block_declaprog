#!/usr/bin/env python


def number_of_unique_letters(txt):
    return len({ch for ch in txt.lower() if ch.isalpha()})


def main():
    str1 = "\\(O_o)/" #1
    str2 = "abc" #3
    str3 = "" #0
    print(number_of_unique_letters(str2))


if __name__ == "__main__":
    main()
