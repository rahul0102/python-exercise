import datetime

name = input("Enter your name")
age = int(input("Age:"))

today = datetime.date.today()
year = today.year

print("hello ", name, "you will turn 100 in ", year + (100-age))
