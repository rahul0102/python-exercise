# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
# Because it would take a long time for you to input the months of various scientists,
# you can use my scientist birthday JSON file. Just parse out the months and draw your histogram.




# need to import at least 3 things to make your
# bokeh plots work
from bokeh.plotting import figure, show, output_file
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
    return Counter(months)
def drawHistogram(months):
    # we specify an HTML file where the output will go
    output_file("plot.html")
    x_categories = []
    x = [i for i in months.keys()]
    y = [j for j in months.values()]
    print("x: ", x, "y: ", y)

    for i in num_to_monthStr.values():
        x_categories.append(i)
    # create a figure
    p = figure(x_range = x_categories)

    # create a histogram
    p.vbar(x=x, top=y, width=0.5)

    # render (show) the plot
    show(p)

birthday_dict = getJsonData()

months = getBirthdayMonthCount(birthday_dict)
drawHistogram(months)
