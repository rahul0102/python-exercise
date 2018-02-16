# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.

def checkPrime(n):
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1
            break
    if flag == 1: print(n," not a prime number")
    else: print(n," is a prime number")

n = int(input("Enter number to check prime:"))
checkPrime(n)
