# Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def removeDuplicates(list1):
    list1.sort()
    set1 = set(list1)
    return list(set1)
def removeDuplicates2(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

list1 =[1,1,1,2,1,3,5,6,8,4,88,8,9,10,25,10,33,63,50]
list1.sort()
print(removeDuplicates(list1))
print(removeDuplicates2(list1))
