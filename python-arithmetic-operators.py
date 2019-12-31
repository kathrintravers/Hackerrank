#!/usr/bin/env python3

def my_add(a, b):
    return a + b


def my_subtract(a, b):
    return a - b


def my_product(a, b):
    return a * b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(my_add(a, b))
    print(my_subtract(a, b))
    print(my_product(a, b))