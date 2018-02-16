# Use the BeautifulSoup and requests Python packages to print out
# a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup
reqObj = requests.get("https://www.nytimes.com/")
reqData = reqObj.text

soupData = BeautifulSoup(reqData,"html.parser")
articles = soupData.find_all("h2","story-heading")
#print(articles)
for tag in articles:
    #print(tag.a.text)
    if tag.a:
        print(tag.a.text)
    else:
        print(tag.contents[0])
