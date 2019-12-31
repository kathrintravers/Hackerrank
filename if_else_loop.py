#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print('weird')
    elif n%2 == 0 and n in range(2,5):
        print('not weird')
    elif n%2 == 0 and n in range (6,21):
        print('weird')
    elif n>20 and n%2 == 0:
        print('not weird') 
    