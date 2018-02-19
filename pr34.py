# load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
# and update the JSON file you have on disk with the scientist’s name.

import json

birthday_dict = {
    "Albert Einstein" : "03/14/1879",
    "Benjamin Franklin" : "01/17/1706",
    "Ada Lovelace" : "12/10/1815",
    "Rahul Raval" : "01/02/1997"
}
def saveJson(data, filename="birthdays.json"):
    with open(filename,"w") as f:
        json.dump(data,f)

def getJsonData(filename = "birthdays.json"):
    with open(filename) as f:
        return json.load(f)

def addNewBirthday(nameKey, birthdayValue):
    global birthday_dict

    birthday_dict[nameKey] = birthdayValue
    saveJson(birthday_dict)

def displayBirthdaysDict(birthday_dict):
    print("\n\nWelcome to the birthday dictionary. We know the birthdays of: ")
    for n in birthday_dict:
        print(n)

def getBirthday(nameKey,birthday_dict):
    if nameKey in birthday_dict:
        print(nameKey.strip(), "'s birthday is ", birthday_dict[nameKey])
    else:
        print("Not Available")


while True:
    dict = getJsonData()
    displayBirthdaysDict(dict)

    print(""" \n\nChose option:
        1 -  Get new bithday
        2 -  Add new birthday
        3 -  Exit
    """)
    op = input()

    if op == '1':
        nameKey = input("Who's birthday do you want to look up?: ").title()
        getBirthday(nameKey, dict)
    elif op == '2':
        nameKey = input("Enter name to add to birthdays List:").title()
        birthdayValue = input("Enter birthday of {}: ".format(nameKey))
        addNewBirthday(nameKey, birthdayValue)

        print("Successfully added.")

    else:  break
