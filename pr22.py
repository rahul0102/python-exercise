# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
#  and print out the results to the screen.

open_file = open("test.txt", "r")
line = open_file.readline()
count = 0
while line:
    print(line)
    count+=1
    line = open_file.readline()
print("Total name: ", count)
