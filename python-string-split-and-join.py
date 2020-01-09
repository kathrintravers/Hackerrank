#!/usr/bin/env python3


def split_and_join(line):
    #a = line.split(" ")
    #b = "-".join(a)
    #return b

    return "-".join(line.split(" "))

if __name__ == '__main__':
    #line = input()
    #result = split_and_join(line)
    #print(result)

    #print(split_and_join(input()))

    print("-".join(input().split(" ")))