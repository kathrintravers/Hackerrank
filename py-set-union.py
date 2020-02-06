#!/usr/bin/env python3


# my_list1 = []
# my_list2 = []

# n1 = int(input())
# a1 = input()
# n2 = int(input())
# a2 = input()

# for i in range(n1):
#     b1 = a1.split(" ")
#     for item in b1:
#         my_list1.append(item)

# for i in range(n2):
#     b2 = a2.split(" ")
#     for item in b2:
#         my_list2.append(item)

# my_set = set(my_list1 + my_list2)

# print(len(my_set))

n1 = int(input())
a1 = input()
n2 = int(input())
a2 = input()


my_set = set(a1.split(" ") + a2.split(" "))

print(len(my_set))