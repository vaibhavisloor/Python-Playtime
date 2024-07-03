from bs4 import BeautifulSoup
import lxml
with open("website.html",encoding="utf-8") as file:
    contents = file.read()

soup=BeautifulSoup(contents,"lxml")
# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#  soup.find() is used to locate the first occurrence of a tag or a group of tags within an HTML or XML document represented by a BeautifulSoup object (soup). 
# for tag in soup.find_all("a"):
    # get Text gets the internal text contained within the a tag
    # print(tag.getText())
    # print(tag.get())
print(soup.find(name="a"))
print(soup.find_all("a"))
    # .select_one()
    # .select()
    # print(tag.get("href"))

