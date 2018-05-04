from bs4 import BeautifulSoup
import re

filename = "Input/Sample DBLP.xml"
source = open(filename,"r")
contents = source.read()
soup = BeautifulSoup(contents,'xml')
keyword = raw_input("Enter the word to be searched: ")
searching = soup.find_all(string = re.compile(keyword, re.IGNORECASE))


for word in searching:
    for x in word.parents:
        if x is None:
            print("end")
        else:
            if x.name == "dblp":
                for i in range(0, len(word.contents)):
                    if i % 2 != 0:
                        print(word.contents[i].name + " : " + word.contents[i].contents[0])
                break
            word = word.parent
            print("\n")
