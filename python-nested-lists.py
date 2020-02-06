#!/usr/bin/env python3



if __name__ == '__main__':

    marksheet = []
    for _ in range(0,int(input())):
        # Create nested marksheet from input
        marksheet.append([input(), float(input())])

    # Sort Marksheet first by score than by name
    marksheet.sort(key= lambda x: (x[1],x[0]))



        