
# load that JSON file from disk, extract the months of all the birthdays,
# and count how many scientists have a birthday in each month.

# Your program should output something like:
#
# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }


import json
from collections import Counter

num_to_monthStr = {
    1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

def getJsonData(filename = "birthdays.json"):
    with open(filename) as f:
        return json.load(f)

def getBirthdayMonthCount(birthday_dict):
    months = []
    for b in birthday_dict.values():
        month = int(b.split('/')[0]) #getting month form birthday format : MM/DD/YYYY
        months.append(num_to_monthStr[month])

    print(Counter(months))

birthday_dict = getJsonData()

getBirthdayMonthCount(birthday_dict)
