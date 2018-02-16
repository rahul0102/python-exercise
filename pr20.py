# Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number. The function decides whether or not the given number
# is inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.

import random

def binarySearch(number_list, n, first, last):
    first = 0
    last = last - 1

    while first <= last:
        mid = int((last+first)/2)
        print("mid:", mid)
        if n == number_list[mid]:
            return mid
        elif n < number_list[mid]:
            last = mid - 1
        elif n > number_list[mid]:
            first = mid + 1
        else:
            pass
    return -1

number_list = random.sample(range(100),10)
number_list.sort()

print("List:" ,number_list)
n = int(input("Enter number to search: "))
result = binarySearch(number_list, n, 0, len(number_list))
print("Result: ", result)
if result == -1:
    print("Unable to find")
else:
    print("Found at position: ", result)
