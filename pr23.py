# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and
# the other .txt file has a list of happy numbers up to 1000.

def readFile(filename):
    open_file = open(filename, "r")
    list1 = []
    line = open_file.readline().strip()
    while line:
        list1.append(line)
        line = open_file.readline().strip()
    return list1

primeNumbers = readFile("prime.txt")
happyNumbers = readFile("happynumbers.txt")

commonNumbers = [n for n in primeNumbers if n in happyNumbers]
print(commonNumbers)
