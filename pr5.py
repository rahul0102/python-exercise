# Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)

def checkPalin(inStr):
    revStr = inStr[::-1]
    print("Reverse is : ", revStr)

    if revStr == inStr: print("palindrome")
    else: print("Not palindrome")
    return

inStr = input("Enter String : ")
checkPalin(inStr)
