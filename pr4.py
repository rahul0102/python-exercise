# write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 10, 11, 12, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55]

c_list=[]
if(len(a) > len(b)):
    for x in a:
        if (x in b) and (x not in c_list):
            c_list.append(x)
else:
    for x in b:
        if (x in a) and (x not in c_list):
            c_list.append(x)
print(c_list)
