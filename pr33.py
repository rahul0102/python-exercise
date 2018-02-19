# For this exercise, we will keep track of when our friend’s birthdays are, and
# be able to find that information based on their name.
# Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name, and return
# the birthday of that person back to them.
# The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

birthday_dict = {
    "Albert Einstein" : "03/14/1879",
    "Benjamin Franklin" : "01/17/1706",
    "Ada Lovelace" : "12/10/1815",
    "Rahul Raval" : "01/02/1997"
}

def getBirthday(nameKey,birthday_dict):
    if nameKey in birthday_dict:
        print(nameKey.strip(), "'s birthday is ", birthday_dict[nameKey])
    else:
        print("Not Available")

def displayBirthdaysDict(birthday_dict):
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for n in birthday_dict:
        print(n)

displayBirthdaysDict(birthday_dict)
nameKey = input("Who's birthday do you want to look up?")
getBirthday(nameKey, birthday_dict)
